# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask.ext.restful import Api, Resource
import handler

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'hello': 'libvirtplus'}


class Containers(Resource):
    def get(self):
        return handler.getAllContainersID()


class Container(Resource):
    def get(self, container_id):
        rtn = handler.getContainerInfoByID(container_id)
        return Flask.json_encoder(rtn)

    def put(self, container_id):
        return

    def post(self, container_id):
        xml = request.form['data']
        return handler.createContainer(xml)

    def delete(self, container_id):
        return handler.deleteContainerByID(container_id)


def apiserver(host='127.0.0.1', port='2376'):
    registry()
    app.run(host=host, port=port)


def registry():
    api.add_resource(Home, '/')
    api.add_resource(Containers, '/containers', endpoint='containers')
    api.add_resource(Container, '/containers/<string:container_id>', endpoint='container')
