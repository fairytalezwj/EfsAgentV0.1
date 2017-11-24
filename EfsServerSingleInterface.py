# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsServerSingleInterface(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self, inf_name):
        return jsonify('get', inf_name)

    def delete(self, inf_name):

        return jsonify('delete', inf_name)

    def post(self, inf_name):
        jreq = request.json
        if 'Data' not in jreq or \
                        type(jreq['Data']) is not dict or \
                        'ServerName' not in jreq['Data'] or \
                        type(jreq['Data']['ServerName']) is not str or \
                        jreq['Data']['ServerName'].strip() == "" or \
                        'InfName' not in jreq['Data'] or \
                        type(jreq['Data']['InfName']) is not str or \
                        jreq['Data']['InfName'].strip() == "" or \
                        'Addr' not in jreq['Data'] or \
                        type(jreq['Data']['Addr']) is not str or \
                        jreq['Data']['Addr'].strip() == "" or \
                        'MacAddr' not in jreq['Data'] or \
                        type(jreq['Data']['MacAddr']) is not str or \
                        jreq['Data']['MacAddr'].strip() == "":
            raise InvalidRequest(100, 400)
        else:
            return jsonify('post', inf_name)
