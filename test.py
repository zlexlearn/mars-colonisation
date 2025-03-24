import requests as r

url = 'http://127.0.0.1:8080/api/jobs'
print(r.get(url).text)
print(r.get(f"{url}/1").text)
print(r.get(f"{url}/99999").text)
print(r.get(f"{url}/string_type").text)
