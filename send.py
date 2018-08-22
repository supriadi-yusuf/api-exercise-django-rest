import requests
import json

headers = {}

# ask for token
member_identity = {'username':'ruli', 'password':'pass1234'} # dictionary

# post parameter : url, files, headers, data/json
# Note, the json parameter is ignored if either data or files is passed.
# data = json.dumps(json_data)
r = requests.post( url='http://127.0.0.1:8000/api/token/', data=member_identity )

#r = requests.get( url='http://127.0.0.1:8000')
token_data = r.json() # convert to json/dictionary

headers['Authorization'] = 'Bearer ' + token_data['access']

print('semua :')
r = requests.get( url='http://127.0.0.1:8000/', headers=headers)
print(r.text)

print('paradigma :')
r = requests.get( url='http://127.0.0.1:8000/paradigma/', headers=headers)
print(r.text)

paradigma = {'name': 'block code'}
print('add new paradigma :')
r = requests.post( url='http://127.0.0.1:8000/paradigma/', headers=headers, data=paradigma)
print(r.text)
new_paradigma = r.json() #convert to dictionary type

print('refresh paradigma :')
r = requests.get( url='http://127.0.0.1:8000/paradigma/', headers=headers)
print(r.text)
#print(type(r.json())) # list of dictionary

print('delete paradigma :')
r = requests.delete( url='http://127.0.0.1:8000/paradigma/' + str(new_paradigma['id']) + '/', headers=headers)
print(r.text)

print('refresh paradigma :')
r = requests.get( url='http://127.0.0.1:8000/paradigma/', headers=headers)
print(r.text)

print('bahasa :')
r = requests.get( url='http://127.0.0.1:8000/bahasa/', headers=headers)
print(r.text)

print('bahasa (20) :')
r = requests.get( url='http://127.0.0.1:8000/bahasa/20', headers=headers)
print(r.text)

print('bahasa (20) after patch :')
data = {'name':'melayu'}
r = requests.patch( url='http://127.0.0.1:8000/bahasa/20/', headers=headers, data=data)
print(r.text)

print('bahasa (20) after put :')
data['paradigm'] = '123'
r = requests.put( url='http://127.0.0.1:8000/bahasa/20/', headers=headers, data=data)
print(r.text)

#r = requests.delete( url='http://127.0.0.1:8000/bahasa/18/', headers=headers)
#print(r.text)

print('bahasa :')
r = requests.get( url='http://127.0.0.1:8000/bahasa/', headers=headers)
print(r.text)
