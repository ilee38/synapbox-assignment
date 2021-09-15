from flask import make_response, jsonify, request, json, abort
from flask.views import MethodView

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
         returns: a message indicating the result of the operation.
      """
      try:
         data = dict(request.json)

         #TODO: implement new node insertion

         return make_response('Data inserted correctly', 200)
      except Exception as error:
         print(error)
         abort(400)
