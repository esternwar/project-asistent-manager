from app import app
import json
from flask import request, jsonify
from app.queries import PrioritySchema

@app.route('/')
def index():
    return 'start'


@app.route('/getJson')
def getJson():
    return json.dumps({"c": 1, "b": 2, "a": 'text'})


@app.route('/setJson', methods=['POST'])
def setJson():
    json_data = request.json
    a_value = json_data["a"]
    print(a_value)

    return 'ok'


@app.route('/property', methods=['GET', 'POST', 'PUT', 'DELETE'])
def property():
    if request.method == 'GET':
        props = PrioritySchema.getProperty()
        return jsonify(props)
    elif request.method == 'POST':
        data = request.json
        res = PrioritySchema.createProperty(data['title'])
    elif request.method == 'PUT':
        data = request.json
        res = PrioritySchema.updateProperty(data['id'], data['title'])
    elif request.method == 'DELETE':
        id = request.args.get('id')
        res = PrioritySchema.removeProperty(id)

    return str(res)