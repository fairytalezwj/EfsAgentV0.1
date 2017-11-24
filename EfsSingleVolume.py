# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify
from handleErrorRequest import *


class EfsSingleVolume(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self, volume_name):
        return jsonify('get', volume_name)
