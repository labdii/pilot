from flask import Flask
from flask import abort
from flask import session
from flask_restful import Api
from functools import wraps
from api.home import Index
from api.api import ApiIndex
from api.users import UserSignUp
from api.users import UserLogin
from api.users import UserLogout
from api.users import UserCheck
from api.users import UserUpdate
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import random
import string

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True

app.config['SECRET_KEY'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))
app.config['MONGODB_URI'] = os.environ['MONGODB_URI']
app.config['MONGODB_DBNAME'] = os.environ['MONGODB_DBNAME']

mongo = PyMongo(app, config_prefix="MONGODB")

api.add_resource(Index, '/')
api.add_resource(ApiIndex, '/api')
api.add_resource(UserSignUp, '/api/users/sign_up', resource_class_kwargs={'mongo' : mongo})
api.add_resource(UserLogin, '/api/users/login', resource_class_kwargs={'mongo' : mongo})
api.add_resource(UserUpdate, '/api/users/update', resource_class_kwargs={'mongo' : mongo})
api.add_resource(UserCheck, '/api/users/check')
api.add_resource(UserLogout, '/api/users/logout')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
