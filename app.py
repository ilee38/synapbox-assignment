from flask import Flask
from src import Tree

"""Main flask app for the REST API.
"""

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello. Submit requests to: /api/end-point'


@app.route('/api')
def hello_world():
   return 'Welcome to our API. Submit requests to: /api/end-point'


app.add_url_rule('/api/tree', view_func=Tree.as_view('tree'))


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=3001)
