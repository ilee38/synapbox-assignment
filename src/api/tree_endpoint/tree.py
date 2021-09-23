from flask import make_response, jsonify, request, json, abort
from flask.views import MethodView
import uuid

class Tree(MethodView):
   """API end-point to perform operations on the tree data.
      path: /api/tree
      methods:
         GET - returns the current tree.
         POST - creates a new entry in the tree.
   """

   def get(self):
      """Handles GET requests.
         returns: the current tree as a JSON object.
      """
      try:
         with open("tree_data.json") as f:
            response = json.load(f)

         return make_response(jsonify(response), 200)
      except Exception as error:
         print(error)
         abort(400)


   def post(self):
      """Handles POST requests: inserts a new node in the tree.
         returns: the id of the newly inserted node
      """
      try:
         data = dict(request.json)
         new_id = str(uuid.uuid4())

         self.insert_node(new_id, data)

         return make_response(jsonify({"id": new_id}), 201)
      except Exception as error:
         print(error)
         abort(400)


   def insert_node(self, new_id, data):
      parent_id = data['parent']
      new_label = data['label']

      with open('tree_data.json') as f:
         tree_data = json.load(f)

      for element in tree_data:
         if isinstance(element, dict):
            self.search_dict(element, parent_id, new_id, new_label)
         elif isinstance(element, list):
            self.search_list(element, parent_id, new_id, new_label)

      self.save_tree(tree_data)


   def search_dict(self, dict_object, parent_id, new_id, new_label):
      for element in dict_object:
         if element == parent_id:
            dict_object[element]['children'].append({new_id: {'label': new_label, 'children': []}})
            break
         elif isinstance(dict_object[element], dict):
            self.search_dict(dict_object[element], parent_id, new_id, new_label)
         elif isinstance(dict_object[element], list):
            self.search_list(dict_object[element], parent_id, new_id, new_label)


   def search_list(self, list_object, parent_id, new_id, new_label):
      for i in range(len(list_object)):
         if isinstance(list_object[i], dict):
            self.search_dict(list_object[i], parent_id, new_id, new_label)


   def save_tree(self, tree_data):
      with open('tree_data.json', 'w') as f:
         f.write(json.dumps(tree_data))