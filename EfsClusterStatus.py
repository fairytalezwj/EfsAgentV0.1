# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask import request, jsonify, abort
from handleErrorRequest import *


class EfsClusterStatus(MethodView):
    def __init__(self):
        if request_authentication() != True:
            raise InvalidRequest(101, 400)

    def get(self):
        return jsonify('EfsClusterStatus')
