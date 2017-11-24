# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsAllExports(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self):

        return jsonify('EfsAllExports')

    def post(self):
        jreq = request.json
        if 'Data' not in jreq or \
                        type(jreq['Data']) is not dict or \
                        'ExportName' not in jreq['Data'] or \
                        type(jreq['Data']['ExportName']) is not str or \
                        jreq['Data']['ExportName'].strip() == "" or \
                        'SecString' not in jreq['Data'] or \
                        type(jreq['Data']['SecString']) is not dict or \
                        jreq['Data']['SecString'].strip() == "" or \
                        'ClientSpec' not in jreq['Data']['SecString'] or \
                        type(jreq['Data']['SecString']['ClientSpec']) is not str or \
                        jreq['Data']['SecString']['ClientSpec'].strip() == "" or \
                        'RW' not in jreq['Data']['SecString'] or \
                        type(jreq['Data']['SecString']['RW']) is not str or \
                        jreq['Data']['SecString']['RW'].strip() == "" or \
                        'User' not in jreq['Data']['SecString'] or \
                        type(jreq['Data']['SecString']['User']) is not str or \
                        jreq['Data']['SecString']['User'].strip() == "" or \
                        'Mode' not in jreq['Data']['SecString'] or \
                        type(jreq['Data']['SecString']['Mode']) is not str or \
                        jreq['Data']['SecString']['Mode'].strip() == "":
            raise InvalidRequest(100, 400)
        else:
            return jsonify('EfsAllExports')
