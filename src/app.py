from flask import Flask, jsonify, request
from flask import json
app = Flask(__name__)



todos = [
    { "label": "My first task", "done": False },
    { "label": "My first task", "done": False },
]

@app.route('/todos', methods=['GET'])
def hello_world():

    json_todos = jsonify(todos)

    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return json_todos




# These two lines should always be at the end of your app.py file.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)