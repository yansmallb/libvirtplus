# -*- coding: UTF-8 -*-
from flask import Flask, request
from flask.ext.restful import Api, Resource
import handler
import plugin
from log import logger

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {'hello': 'libvirtplus'}


class Containers(Resource):
    def get(self):
        logger.info('Get containers ID list')
        list = handler.getAllContainersID()
        logger.info(list)
        return list

    def post(self):
        logger.info('Create container')
        xml = request_to_xml(request)
        logger.debug('Container xml is {xml}'.format(xml=xml))
        strID = handler.createContainer(xml)
        logger.info('Created success,ID is {strID}'.format(strID=strID))
        return strID


class Container(Resource):
    def get(self, container_id):
        logger.info('Get container {container_id}'.format(container_id=container_id))
        rtn = handler.getContainerInfoByID(container_id)
        return rtn

    def put(self, container_id):
        logger.info('Update container {container_id}'.format(container_id=container_id))
        xml = request_to_xml(request)
        logger.debug('Container xml is {xml}'.format(xml=xml))
        return handler.updateContainer(xml, container_id)

    def post(self, container_id):
        logger.info('Post container {container_id}, do nothing.'.format(container_id=container_id))
        return "please use post with url: /containers or use put with url: /containers/<container_id>"

    def delete(self, container_id):
        logger.info('Delete container {container_id}'.format(container_id=container_id))
        return handler.deleteContainerByID(container_id)


def start_server(host='127.0.0.1', port='2376'):
    logger.info('Start libvirtplus server in:{host}:{port}'.format(host=host, port=port))
    registry()
    app.run(host=host, port=port)
    #app.run(host=host, port=port, debug=True, use_reloader=False)


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
