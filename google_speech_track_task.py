#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

AuthoID=input("Please input your autho ID \n")
mission_code=input("please type your mission_code \n")

url = 'https://speech.googleapis.com/v1/operations/' + mission_code + '/?key=' + AuthoID
headers = {'content-type': 'application/json'}

after_call = requests.get(url, headers=headers)

paragnum = int(0)
text=json.loads(after_call.text)
resu1=len((text['response']['results']))


while paragnum < resu1:
    if after_call.status_code == 200:
        print(((((((text['response']['results'][paragnum]['alternatives'][0]['transcript'])))))))
        paragnum = paragnum +1
    else:
        print("error, pls check the id or code you type in")
        text=json.loads(after_call.text)
        print (text)
