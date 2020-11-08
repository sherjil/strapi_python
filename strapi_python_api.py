import requests, json

########## GET JWT TOKEN ##########

auth = { 'identifier' : '<email or username>', 'password' : '<password>' }
r = requests.post('http://<Server IP>:1337/auth/local', data=auth)
print(r.json())
tokenAuth = r.json()
print(tokenAuth['jwt'])
token = 'Bearer ' + tokenAuth['jwt']




########## CHECK TOKEN VALIDTY ##########

response = requests.get('http://<Server IP>:1337/restaurants/count', headers={ 'Authorization': token })
print(response.text)

# if you get for permissions on authenticated user to get count if you get error




########## ADD DATA ##########

rest = {"name":"Pak","description":"Authenticad Pakistani Food"}
response1 = requests.post('http://<Server IP>:1337/restaurants', headers={ 'Authorization': token }, data=rest)
print(response1.text)




########## UPLOAD IMAGE/FILE ##########

url = 'http://<Server IP>:1337/upload'
files = {'files': ('<Your File Name>.jpg', open('<Your File Location>.jpg','rb'), 'image/jpg')}
response2 = requests.post(url, headers={ 'Authorization': token }, files=files)
print(response2.text)

# Make sure about authenticated user have permissions to upload
