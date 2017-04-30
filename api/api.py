from flask import jsonify
from flask_restful import Resource


class ApiIndex(Resource):

    def post(self):

        return jsonify({
    	    "ping": "pong",
            "enterprise": "Labdii Inc.",
            "api_version": "1.0"
        })

    def get(self):

        return jsonify({
    	    "ping": "pong",
            "enterprise": "Labdii Inc.",
            "api_version": "1.0"
        })
