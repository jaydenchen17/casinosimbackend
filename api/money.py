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

class MoneyAPI:
    class _Test(Resource):
        def get(self):
            response = jsonify({"Connection Test": "Successfully connected to backend!"})
            return response
       
api.add_resource(MoneyAPI._Test, '/test')

if __name__ == "__main__":
    server = "http://127.0.0.1:8987" # run local
    # server = 'https://chat.stu.nighthawkcodingsociety.com'  # Update with your server URL
    url = server + "/api/money"
    responses = []
