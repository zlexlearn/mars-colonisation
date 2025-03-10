from sqlalchemy import String as Str, Integer as Int, Column as Col, ForeignKey, Boolean, DateTime
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Col(Int, primary_key=True, nullable=False)
    team_leader = Col(Int, ForeignKey('users.id'))
    job = Col(Str, nullable=False)
    work_size = Col(Int, nullable=False)
    collaborators = Col(Str, nullable=False)
    start_date = Col(DateTime, nullable=False)
    end_date = Col(DateTime, nullable=False)
    is_finished = Col(Boolean, nullable=False)

    user = orm.relationship('User')
