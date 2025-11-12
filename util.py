import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

BASE_URL = "https://cad.onshape.com/api/v10"
ACCESS_KEY = os.getenv("ONSHAPE_ACCESS_KEY")
SECRET_KEY = os.getenv("ONSHAPE_SECRET_KEY")



params = {}

headers = {'Accept': 'application/json;charset=UTF-8;qs=0.09',
           'Content-Type': 'application/json'}

def document_GET(api_endpoint):
    response = {}
    response = requests.get(
        BASE_URL + "/documents" + api_endpoint,
        params = params,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers=headers)
        
    return response

def document_POST(api_endpoint, payload):
    response = requests.post(
        BASE_URL + "/documents" + api_endpoint,
        json=payload,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers=headers
    )
    
    return response

def document_DELETE(api_endpoint):
    response = requests.delete(
        BASE_URL + "/documents" + api_endpoint,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers=headers
    )

    return response

def partstudio_GET(api_endpoint):
    response = {}
    response = requests.get(
        BASE_URL + "/partstudios" + api_endpoint,
        params = params,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers=headers)
        
    return response

def partstudio_POST(api_endpoint, payload):
    response = requests.post(
        BASE_URL + "/partstudios" + api_endpoint,
        json=payload,
        auth=(ACCESS_KEY, SECRET_KEY),
        headers=headers
    )
    
    return response


# def document_CRUD(HTTPrequest, api_endpoint, payload):
#     # response = {}
#     if(HTTPrequest == 'GET'):
#         response = requests.get(BASE_URL + "/documents" + api_endpoint, 
#                             params=params, 
#                             auth=(ACCESS_KEY, SECRET_KEY),
#                             headers=headers)
        
#         return response
#     if(HTTPrequest == 'POST'):
#         # payload = {
#         #     "name": "New API Document",
#         #     "description": "Created via Python script"
#         # }

#         response = requests.post(
#             BASE_URL + "/documents" + api_endpoint,
#             json=payload,
#             auth=(ACCESS_KEY, SECRET_KEY),
#             headers=headers)
        
#         return response
    
#     return None
    

#     # return response.json()