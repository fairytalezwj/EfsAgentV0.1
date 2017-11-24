# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsSingleExport(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self, export_name):
        return jsonify(export_name)

    def delete(self, export_name):
        return jsonify('delete', export_name)

