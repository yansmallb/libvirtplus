# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask.ext.restful import Api, Resource
import handler
import plugin

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'hello': 'libvirtplus'}


class Containers(Resource):
    def get(self):
        return handler.getAllContainersID()

    def post(self):
        xml = request_to_xml(request)
        return handler.createContainer(xml)


class Container(Resource):
    def get(self, container_id):
        rtn = handler.getContainerInfoByID(container_id)
        return rtn

    def put(self, container_id):
        xml = request_to_xml(request)
        return handler.updateContainer(xml, container_id)

    def post(self):
        return "please use post with url: /containers "

    def delete(self, container_id):
        return handler.deleteContainerByID(container_id)


def start_server(host='127.0.0.1', port='2376'):
    registry()
    #app.run(host=host, port=port)
    app.run(host=host, port=port, debug=True, use_reloader=False)


def registry():
    api.add_resource(Home, '/')
    api.add_resource(Containers, '/containers', endpoint='containers')
    api.add_resource(Container, '/containers/<string:container_id>', endpoint='container')


def request_to_xml(request):
    dicts = {'name': request.form.get('name'), 'memory': request.form.get('memory'),
             'cdrom_source': request.form.get('cdrom_source'), 'disk_source': request.form.get('disk_source'),
             'vcpu': request.form.get('vcpu'), 'boot': request.form.get('boot')}
    if dicts['name'] is None:
        dicts = plugin.json_to_dict(request.data)
    return plugin.dict_to_xml(dicts)
