from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Column as Col, Integer as Int, String as Str, DateTime, orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = Col(Int, primary_key=True, autoincrement=True)
    surname = Col(Str, nullable=False)
    name = Col(Str, nullable=False)
    age = Col(Int, nullable=False)
    position = Col(Str, nullable=False)
    speciality = Col(Str, nullable=False)
    address = Col(Str, nullable=False)
    email = Col(Str, nullable=False, unique=True)
    hashed_password = Col(Str, nullable=False)
    modified_date = Col(DateTime, nullable=False, default=datetime.now)

    jobs = orm.relationship('Jobs', back_populates='user')

    def __repr__(self):
        return f"<Colonist> {self.id} {self.surname} {self.name}"

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return password == self.hashed_password

    