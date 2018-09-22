#!/usr/local/bin/python3

import requests
import json

headers = {'username':'ruli', 'password':'pass1234'} # dictionary

#r = requests.post( url='http://127.0.0.1:8000/api/token/', data=member_identity )
#print(r.text)

r = requests.get( url='http://127.0.0.1:8000/', headers=headers )
print(r.text)

r = requests.get( url='http://127.0.0.1:8000/bahasa/', headers=headers )
print(r.text)

r = requests.get( url='http://127.0.0.1:8000/bahasa/20/', headers=headers )
print(r.text)

# http://127.0.0.1:8000/api-auth/logout/
