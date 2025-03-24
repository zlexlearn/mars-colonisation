from flask import jsonify, abort
from flask_restful import Resource, reqparse

from data.db_session import create_session
from data.users import User

praser = reqparse.RequestParser()
praser.add_argument('surname', required=False)
praser.add_argument('name', required=False)
praser.add_argument('age', required=False, type=int)
praser.add_argument('position', required=False)
praser.add_argument('speciality', required=False)
praser.add_argument('address', required=False)
praser.add_argument('email', required=False)
praser.add_argument('hashed_password', required=False)


# api/users/<id>
class UserResourse(Resource):
    def get(self, user_id):
        s = create_session()
        user = s.query(User).filter(User.id == user_id).first()
        if not user:
            return abort(404, 'Not found')
        return jsonify(user.to_dict(
            only=(
                "id",
                "surname",
                "name",
                "age",
                "position",
                "speciality",
                "address",
                "email",
                "hashed_password",
                "modified_date",
            )
        ))

    def delete(self, user_id):
        s = create_session()
        user = s.query(User).filter(User.id == user_id).first()
        if not user:
            return abort(404, 'Not found')
        s.delete(user)
        s.commit()
        return jsonify({"status": 'ok'})

    def post(self):
        pass


class UserListResourse(Resource):
    def get(self):
        s = create_session()
        users = s.query(User).all()
        return jsonify([user.to_dict(
            only=(
                "id",
                "surname",
                "name",
                "age",
                "position",
                "speciality",
                "address",
                "email",
                "hashed_password",
                "modified_date",
            )
        ) for user in users])

    def post(self):
        args = praser.parse_args()
        s = create_session()
        user = User(**args)
        s.add(user)
        s.commit()
        return jsonify({"user_id": user.id})


# import requests as r
#
# url = 'http://127.0.0.1:8080/api/users'
#
# resp = r.post(url, json={
#     'surname': 'bla bla bla',
#     'name': 'bla bla bla',
#     'age': 30,
#     'position': 'dev',
#     'speciality': 'back',
#     'address': '123 psk msc',
#     'email': 'a.b@123.com',
#     'hashed_password': '123'
# })
# print(f"{resp.text}")
#
# resp = r.get(url)
# print(f"{resp.text}")
#
# resp = r.get(f'{url}/1')
# print(f"{resp.text}")
#
# resp = r.delete(f'{url}/1')
# print(f"{resp.text}")
#
# resp = r.post(url, json={
#     'surname': 'a',
#     'name': 'b',
#     'age': 'тридцать',  # str
#     'position': 'dev',
#     'speciality': 'backen',
#     'address': '123 Main St',
#     'email': 'ab.b@ex.com',
#     'hashed_password': '123'
# })
# print(f"{resp.text}")
#
# resp = r.post(url, json={
#     'surname': 'd',
#     'name': 'asd',
#     'age': 30,
#     'position': 'dev',
#     'speciality': 'backend',
#     'address': '123 Main St',
#     'email': 'ads.ads@asd.com',
#     'hashed_password': 'dasd',
#     'f': '123'
# })
# print(f"{resp.text}")
#
# resp = r.get(f'{url}/94032393013')  # 404
# print(f"{resp.text}")
#
# resp = r.delete(f'{url}/89128391312')  # 404
# print(f"{resp.text}")
