import http.client
import json
import threading

conn = http.client.HTTPConnection("localhost",8000)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
data2 = data1
print(data1)

while True:
    conn.request("GET", "/")
    r1 = conn.getresponse()
    data1 = r1.read().decode()
    if data2 != data1:
        print(r1.status, r1.reason)
        print(data1)
        data2 = data1
    headers = {'Content-type': 'application/json'}
    message = input("Ingrese el mensaje")
    foo = {'text': f'{message}'}
    json_data = json.dumps(foo)
    conn.request('POST', '/post', json_data, headers)
    r1 = conn.getresponse()
    data1 = r1.read().decode()
    if(data2 != data1):
        data2 = data1

