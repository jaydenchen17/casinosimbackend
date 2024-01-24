from flask import Blueprint, request, jsonify  
from flask_restful import Api, Resource 
from flask_cors import CORS
import requests  
from model.moneys import *

money_api = Blueprint('money_api', __name__,
            url_prefix='/api/money')
api = Api(money_api)

CORS(money_api, resources={r"/api/money/create": {"origins": "http://127.0.0.1:8987"}})

chat_data = []

class ChatAPI:
    class _Test(Resource):
        def get(self):
            response = jsonify({"Connection Test": "Successfully connected to backend!"})
            return response
       
api.add_resource(ChatAPI._Test, '/test')

if __name__ == "__main__":
    server = "http://127.0.0.1:8987" # run local
    # server = 'https://chat.stu.nighthawkcodingsociety.com'  # Update with your server URL
    url = server + "/api/money"
    responses = []

    # Simulate sending data to the chat API
    sample_data = {"message": "Hello, this is a test message!"}
    create_response = requests.post(url+"/create", json=sample_data)
    responses.append(create_response)

    # Retrieve stored data from the chat API
    read_response = requests.get(url+"/read")
    responses.append(read_response)

    # Display responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
