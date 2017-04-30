from flask import request
from flask import session
from flask import jsonify
from flask_restful import Resource


class Index(Resource):

    def get(self):

        return jsonify({
    	    "ping": "pong",
            "enterprise": "Labdii Inc."
        })

    def post(self):

        return jsonify({
    	    "ping": "pong",
            "enterprise": "Labdii Inc."
        })
