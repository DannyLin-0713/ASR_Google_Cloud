#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64

AuthoID=input("Please input your autho ID \n")
audio_name=input("Please input your audio name \n")
channel_count=int(input("please type the channle num \n"))

# encode to base64 first, then trnasfer to utf-8 str to aviod the problem of format
audio_b = str(base64.b64encode(open(audio_name,"rb").read()),'utf8')

url = 'https://speech.googleapis.com/v1/speech:longrunningrecognize?key=' + AuthoID
headers = {'content-type': 'application/json'}
requestData={
"config":
{
"encoding":"FLAC",
"languageCode":"en-US",
"audioChannelCount": channel_count,
"enableSeparateRecognitionPerChannel": False,
    "enableAutomaticPunctuation": True
},
"audio":
{
"content": audio_b
} 
}

after_call = requests.post(url, json=requestData, headers=headers)

if after_call.status_code == 200:
    print(after_call)
    text=json.loads(after_call.text)
    trans_code=(text['name'])
    print (text)
else:
    print("error, pls check the file or your autho id")
    text=json.loads(after_call.text)
    print (text)
