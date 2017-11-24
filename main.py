# -*- coding: utf-8 -*-

from initalAgentServer import *
from flask import jsonify, request
from EfsSingleExport import *
from EfsAllExports import *
from EfsClusterStatus import *
from EfsServer import *
from EfsServerAllRoutes import *
from EfsServerSingleRoute import *
from EfsServerAllInterfaces import *
from EfsServerSingleInterface import *
from EfsAllPools import *
from EfsSinglePool import *
from EfsAllVolumes import *
from EfsSingleVolume import *
from EfsResizeVolume import *


@agentServer.route('/')
def hello():
    return jsonify('hello')


def register_view(view_class, http_methods, http_path):
    view_funcc = view_class.as_view(http_path)
    agentServer.add_url_rule(http_path, view_func=view_funcc, methods=http_methods)


def build_agentserver_route():
    register_view(EfsClusterStatus, ['GET'], '/status')

    register_view(EfsAllExports, ['GET', 'POST'], '/exports')
    register_view(EfsSingleExport, ['GET', 'DELETE'], '/exports/:<string:export_name>')

    register_view(EfsServer, ['GET'], '/efserver')

    register_view(EfsServerAllRoutes, ['GET', 'POST'], '/efserver/routes')
    register_view(EfsServerSingleRoute, ['GET', 'DELETE'], '/efserver/routes/:<string:destination>')

    register_view(EfsServerAllInterfaces, ['GET'], '/efserver/interfaces')
    register_view(EfsServerSingleInterface, ['GET', 'POST', 'DELETE'], '/efserver/interfaces/:<string:inf_name>')

    register_view(EfsAllPools, ['GET'], '/pools')
    register_view(EfsSinglePool, ['GET'], '/pools/:<string:pool_name>')

    register_view(EfsAllVolumes, ['GET','POST'], '/volumes')
    register_view(EfsSingleVolume, ['GET'], '/volumes/:<string:volume_name>')
    register_view(EfsResizeVolume, ['POST'], '/volumes/:<string:volume_name>/resize')


if __name__ == '__main__':
    build_agentserver_route()
    agentServer.run(host=agentServerURL, port=agentServerPort)
