from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class itemlist(Resource):
    def get(self, itemname):
        return {itemname : "comb, cookies, earphones, chair, table"}

class item(Resource):
    def get(self, name):
        return {"item" : name}

    def post(self, name):
        if name == "comb" :
            return {"price" : "5.99"}
        elif name == "cookies" :
            return {"price" : "10.99"}
        elif name == "earphones" :
            return {"price" : "15.99"}
        elif name == "chair" :
            return {"price" : "20.99"}
        elif name == "table" :
            return {"price" : "25.99"}

    def put(self, name):
        if name == "comb" :
            return {"price" : "10.99"}
        elif name == "cookies" :
            return {"price" : "15.99"}
        elif name == "earphones" :
            return {"price" : "20.99"}
        elif name == "chair" :
            return {"price" : "25.99"}
        elif name == "table" :
            return {"price" : "30.99"}


api.add_resource(itemlist, '/<string:itemname>')
api.add_resource(item, '/item/<string:name>')

app.run(port=5000)
# RAE553_201AEM012
