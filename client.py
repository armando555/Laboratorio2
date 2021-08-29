import http.client
import json
import threading

#establize connection with localhost in port 8000
conn = http.client.HTTPConnection("localhost",8000)

USER = input('Por favor ingrese su nombre de usuario: ')

conn.request("GET", "/")
firstResponse = conn.getresponse()
currentData = firstResponse.read().decode()
lastData = currentData

print('Start sending messages to the chatroom!!')

while True:
    conn.request("GET", "/")
    firstResponse = conn.getresponse()
    currentData = firstResponse.read().decode()
    
    if lastData != currentData:
        #print(firstResponse.status, firstResponse.reason)
        info = json.loads(currentData)
        print(info["messages"][-1][0] + '> ' + info["messages"][-1][1])
        lastData = currentData

    headers = {'Content-type': 'application/json'}
    message = input('')

    foo = {'text': f'{message}', 'user': f'{USER}'}
    json_data = json.dumps(foo)
    conn.request('POST', '/post', json_data, headers)
    firstResponse = conn.getresponse()
    currentData = firstResponse.read().decode()
    if(lastData != currentData):
        lastData = currentData

