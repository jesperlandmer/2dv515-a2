from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        return {'employees': 'hej'} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        result = {'data': 'data'}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        result = {'data': 'data'}
        return jsonify(result)
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')