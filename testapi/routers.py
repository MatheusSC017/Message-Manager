from flask import Response
from flask_restful import Resource
import json


def initialize_routes(api):
    api.add_resource(EmailMessages, '/email/')
    api.add_resource(WhatsappMessages, '/whatsapp/')


class EmailMessages(Resource):
    def get(self):
        email_json = json.load(open("email_messages.json"))
        print(email_json)
        return Response(json.dumps(email_json), mimetype='application/json', status=200)


class WhatsappMessages(Resource):
    def get(self):
        whatsapp_json = json.load(open("whatsapp_messages.json"))
        return Response(json.dumps(whatsapp_json), mimetype='application/json', status=200)
