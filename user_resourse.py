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
