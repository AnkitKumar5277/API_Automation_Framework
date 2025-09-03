# Pre built methods for GET,POST,PATCH ,PUT and DELETE
import json

import requests

# GET Request
def get_request(url, auth,in_json):
    get_response = requests.get(url=url, auth=auth)
    if in_json:
        return get_response.json()
    return get_response

#POST request
def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json:
        return post_response.json()
    return post_response
#PATCH request
def patch_request(url,auth,headers,payload,in_json):
    patch_response=requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response
#PUT request
def put_request(url,auth,headers,payload,in_json):
    put_response=requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json==True:
        return put_response.json()
    return put_response
#Delete request
def delete_request(url,auth,headers,in_json):
    delete_response=requests.delete(url=url,auth=auth,headers=headers)
    if in_json is True:
        return delete_response.json()
    return delete_response