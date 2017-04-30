from flask import request
from flask import session
from flask import jsonify
from flask_restful import Resource


class UserSignUp(Resource):

    def __init__(self, mongo):
        self.mongo = mongo

    def post(self):

        username_req = request.form.get("username", None)
        password_req = request.form.get("password", None)
        role = request.form.get("role", None)

        not_none = username_req is not None and password_req is not None and role is not None

        if not_none:
            users = [user for user in self.mongo.db.users.find({"username": username_req})]

            if users.__len__() > 0:
                return jsonify({
                    "status": 400,
                    "msg": "user already exists"
                })

            else:
                new_user = self.mongo.db.users.insert_one({
                    "username": username_req,
                    "password": password_req,
                    "role": role
                })

                return jsonify({
                    "new_user_id": new_user.inserted_id.__str__(),
                    "status": 200,
                    "msg": "User registered successful"
                })

        else:
            return jsonify({
                "status": 400,
                "msg": "wrong parameters"
            })


class UserLogin(Resource):

    def __init__(self, mongo):
        self.mongo = mongo

    def post(self):

        username_req = request.form.get("username", None)
        password_req = request.form.get("password", None)

        query = [user for user in self.mongo.db.users.find({"username": username_req, "password": password_req})]

        if query.__len__() == 1:

            query = query[0]

            user_id = query["_id"].__str__()
            username = query["username"]
            password = query["password"]
            role = query["role"]

            auth = username_req == username and password_req == password

            if auth and "username" not in session:
                session["user_id"] = user_id
                session["username"] = username
                session["role"] = role

                return jsonify({
                    "status": 200,
                    "msg": "Authentication successful"
                })

            elif auth and "username" in session:

                return jsonify({
                    "status": 200,
                    "msg": "User already logged"
                })

        else:
            return jsonify({
                "status": 400,
                "msg": "Authentication failed"
            })


class UserLogout(Resource):

    def post(self):
        if "username" in session:
            session.pop("user_id")
            session.pop("username")
            session.pop("role")
            return jsonify({
                "status": 200,
                "msg": "logout successful"
            })
        else:
            return jsonify({
                "status": 400,
                "msg": "not user logged"
            })


class UserCheck(Resource):

    def post(self):
        if "username" in session:
            return jsonify({
                "status": 200,
                "msg": "user logged",
                "current_user_id": "{}".format(session["user_id"]),
                "current_user": "{}".format(session["username"]),
                "role": "{}".format(session["role"])
            })
        else:
            return jsonify({
                "status": 400,
                "msg": "not user logged"
            })


class UserUpdate(Resource):

    def __init__(self, mongo):
        self.mongo = mongo

    def post(self):

        if "username" in session and "role" in session:
            if session["role"] == "admin":

                username_req = request.form.get("username", None)
                password_req = request.form.get("password", None)
                role = request.form.get("role", None)

                query_update = {"$set": dict()}

                if password_req is not None:
                    query_update["$set"]["password"] = password_req

                if role is not None:
                    query_update["$set"]["role"] = role

                if query_update.__len__() > 0:
                    result = self.mongo.db.users.update_one({"username": username_req}, query_update)
                    if result:
                        return jsonify({
                            "status": 200,
                            "msg": "user updated",
                            "fields_updated": [field for field in query_update["$set"].keys()]
                        })
                    else:
                        return jsonify({
                            "status": 400,
                            "msg": "user not found"
                        })

                else:
                    return jsonify({
                        "status": 400,
                        "msg": "not enough paramenters"
                    })

            else:
                return jsonify({
                    "status": 400,
                    "msg": "not authorized"
                })

        else:
            return jsonify({
                "status": 400,
                "msg": "login as admin user"
            })
