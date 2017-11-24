# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsAllVolumes(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self):
        return jsonify('EfsAllVolumes')

    def post(self):
        jreq = request.json
        if 'Data' not in jreq or \
                        type(jreq['Data']) is not dict or \
                        'ServerName' not in jreq['Data'] or \
                        type(jreq['Data']['ServerName']) is not str or \
                        jreq['Data']['ServerName'].strip() == "" or \
                        'PoolName' not in jreq['Data'] or \
                        type(jreq['Data']['PoolName']) is not str or \
                        jreq['Data']['PoolName'].strip() == "" or \
                        'Volname' not in jreq['Data'] or \
                        type(jreq['Data']['Volname']) is not str or \
                        jreq['Data']['Volname'].strip() == "" or \
                        'VolType' not in jreq['Data'] or \
                        type(jreq['Data']['VolType']) is not str or \
                        jreq['Data']['VolType'].strip() == "" or \
                        jreq['Data']['VolType'] != "nfs" or \
                        jreq['Data']['VolType'] != "cifs" or \
                        'Size' not in jreq['Data'] or \
                        type(jreq['Data']['Size']) is not int:
            raise InvalidRequest(100, 400)
        else:
            return jsonify('Add Volume')
