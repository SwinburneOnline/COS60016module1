import requests

#GET
response = requests.get(url='http://127.0.0.1:8000/our_endpoints/server_time')
print(response.text)


#POST
#files = {'text':('test.txt', open('test.txt', 'rb'))}
#print(response.status_code)

files = {'text':('test1.txt', open('test01.txt', 'rb'))}
response = requests.post(url='http://127.0.0.1:8000/our_endpoints/upload_file/', files=files)

print("STATUS CODE: ", response.status_code)
print("CONTENT: ", response.content)


#HEAD
response = requests.head(url='http://127.0.0.1:8000/our_endpoints/status/')
print(response.status_code)


#PUT
payload = '{"record": "NEW_RECORD"}'
response = requests.put(url='http://127.0.0.1:8000/our_endpoints/save_json_to_file/', data=payload)

print(response.text)


#DELETE
file_to_delete = '{"file_name":"test02"}'
response = requests.delete(url='http://127.0.0.1:8000/our_endpoints/delete_file/', data=file_to_delete)

print(response.text)


#PATCH
patch_data = '{"updates":"Some new Stuff"}'
response = requests.patch(url='http://127.0.0.1:8000/our_endpoints/update_file/', data=patch_data)

print(response.text)


#TEST from
response = requests.get(url='http://127.0.0.1:8000/our_endpoints/check_connection')
print(response.check_connection)
#TEST to

