import requests as r

url = 'http://127.0.0.1:8080/api/jobs'

print(r.post(  # true req
    url, json={
        'team_leader': 1,
        'job': 'job desc',
        'work_size': 50,
        'collaborators': 2,
        'is_finished': False,
    }
).text)

print(r.post(
    url, json={'lalalalla': 1}  # bad json
).text)

print(r.post(
    url, json=None  # null json
).text)

print(r.post(
    url, json={
        'team_leader': 'string',  # str, not int
        'job': 18 ** 2,  # int, not a str
        'work_size': 'string',  # str, not int
        'collaborators': None,  # none ,not int
        'is_finished': 'net',  # str, not bool
    }
).text)
