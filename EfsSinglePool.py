# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsSinglePool(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self, pool_name):
        return jsonify('get', pool_name)
