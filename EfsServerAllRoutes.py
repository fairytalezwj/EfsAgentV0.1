# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsServerAllRoutes(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self):
        return jsonify('get EfsServerAllRoutes')

    def post(self):

        jreq = request.json
        if 'Data' not in jreq or \
                        type(jreq['Data']) is not dict or \
                        'Destination' not in jreq['Data'] or \
                        type(jreq['Data']['Destination']) is not str or \
                        jreq['Data']['Destination'].strip() == "" or \
                        'Netmask' not in jreq['Data'] or \
                        type(jreq['Data']['Netmask']) is not str or \
                        jreq['Data']['Netmask'].strip() == "" or \
                        'Gateway' not in jreq['Data'] or \
                        type(jreq['Data']['Gateway']) is not str or \
                        jreq['Data']['Gateway'].strip() == "" or \
                        'Interface' not in jreq['Data'] or \
                        type(jreq['Data']['Interface']) is not str or \
                        jreq['Data']['Interface'].strip() == "":
            raise InvalidRequest(100, 400)
        else:
            return jsonify('add EfsServerAllRoutes')
