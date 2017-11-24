# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsServerSingleRoute(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self, destination):
        return jsonify('get', destination)

    def delete(self, destination):
        return jsonify('delete', destination)
