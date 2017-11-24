from initalAgentServer import agentServer
from flask import jsonify, make_response, request
from common import *
import configparser


class InvalidRequest(Exception):
    status_code = 400

    def __init__(self, error_code=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.error_code = error_code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['ErrorCode'] = self.error_code
        rv['Message'] = ErrorCode[self.error_code]
        return rv


@agentServer.errorhandler(InvalidRequest)
def handle_invalid_request(error):
    response = make_response(jsonify(error.to_dict()))
    response.status_code = error.status_code
    return response

@agentServer.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'ErrorCode':400,'Message':'Bad Request'}),400)

@agentServer.errorhandler(404)
def not_find(error):
    return make_response(jsonify({'ErrorCode':404,'Message':'Not Found'}),404)

@agentServer.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'ErrorCode':405,'Message':'Method Not Allowed'}),405)

@agentServer.errorhandler(500)
def not_find(error):
    return make_response(jsonify({'ErrorCode':500,'Message':'Internal Server Error'}),500)



def request_authentication():
    json_req = request.json
    # print(json_req)
    # print(type(json_req['Authentication']['Account']))
    if not request.json or \
                    'Authentication' not in json_req or \
                    type(json_req['Authentication']) is not dict or \
                    type(json_req['Authentication']['Account']) is not str or \
                    type(json_req['Authentication']['Password']) is not str:
        return False

    conf = configparser.ConfigParser()
    if conf.read('conf.ini'):
        Account = conf.get('keyring', 'Account')
        Password = conf.get('keyring', 'Password')

        if json_req['Authentication']['Account'] == Account and \
                        json_req['Authentication']['Password'] == Password:
            return True

    else:
        return False
