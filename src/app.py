from flask import Flask
import flask 
from flask import request
import json
app = Flask(__name__)

# todos global variable
todos = [
    {"label": "Study Flask", "done": False},
    {"label": "Work on final project", "done": False}
]

# declaring get endpoint
@app.route('/todos', methods=['GET'])
def hello_world():
    # convert the variable into a json string
    todos_text = flask.jsonify(todos)
    return todos_text

# post endpoint
@app.route('/todos', methods=['POST'])
def add_new_todo():

    # asking for the data
    request_body = request.data

    # 1. converting json string into real python object or decoding json string
    decoded_object = json.loads(request_body)

    # 2. add decoded object into todos list
    todos.append(decoded_object)

    # 3. return jsonify list updated of todos
    print("Incoming request with the following body", request_body)
    return flask.jsonify(todos)
    
# delete endpoint
# When you use the symbols < and > Flask will return whatever the client specified on that part the URL as a variable
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    # remove the task with pop method
    todos.pop(position)
    print("This is the position to delete:", position)
    # return a new list as json string
    return flask.jsonify(todos)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)