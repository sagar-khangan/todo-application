from flask import Blueprint, request, jsonify
from flask_cors import CORS
from todo.helpers import create, retrieve, update, delete

todo = Blueprint('todo', __name__)
CORS(todo)


@todo.route('/<list_id>/<task_id>', methods=('PUT', 'DELETE'))
@todo.route('/<list_id>', methods=('GET', 'POST'))
def home(list_id,task_id=None):
    try:
        data = dict()
        if request.method == 'GET':
            data,_success = retrieve(list_id)
        elif request.method == 'POST':
            _data = request.json
            data,_success = create(list_id,_data)
        elif request.method == 'PUT':
            _data = request.json
            data,_success = update(list_id,task_id, _data)
        elif request.method == 'DELETE':
            data,_success = delete(list_id,task_id)
        if _success:
            resp = {"status": "Success", "data": data}
        else:
            resp = {"status": "Fail", "data": data}
    except:
        resp = {"status":"Fail","data":"Something went wrong"}
    return jsonify(resp)
