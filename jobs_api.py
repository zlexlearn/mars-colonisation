from flask import Blueprint, jsonify, request, make_response

from data import db_session
from data.jobs import Jobs

bl = Blueprint('jobs_api', __name__, template_folder='templates')


@bl.route('/api/jobs/<job_id>')
def get_job(job_id):
    s = db_session.create_session()
    job = s.query(Jobs).filter(Jobs.id == job_id).first()
    return jsonify(job.to_dict(only=(
        'id', 'user.name', 'job', 'is_finished', 'end_date', 'start_date', 'collaborators', 'work_size'
    )))


@bl.route('/api/jobs')
def get_jobs():
    s = db_session.create_session()
    jobs_lst = s.query(Jobs).all()
    return jsonify({'jobs': [j.to_dict(only=(
        'id', 'user.name', 'job', 'is_finished', 'end_date', 'start_date', 'collaborators', 'work_size'
    )) for j in jobs_lst]})


@bl.route('/api/jobs', methods=['POST'])
def create_job():
    print(request.json)
    if not request.json:
        return make_response(jsonify({"error": "Not found"}), 404)
    columns = ['team_leader', 'job', 'collaborators', 'is_finished', 'work_size']
    if not all([col in request.json for col in columns]):
        return make_response(jsonify({"error": "Bad Request"}), 400)
    s = db_session.create_session()
    job = Jobs()
    for col in columns:
        setattr(job, col, request.json[col])
    s.add(job)
    s.commit()
    return jsonify({"success": 200})
