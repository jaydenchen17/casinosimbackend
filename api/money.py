from flask import Blueprint, request, jsonify  
from flask_restful import Api, Resource 
from flask_cors import CORS
from auth_middleware import token_required  # Assuming you have implemented this middleware

money_api = Blueprint('money_api', __name__, url_prefix='/api/money')
api = Api(money_api)

CORS(money_api, resources={r"/api/money/*": {"origins": "http://127.0.0.1:8987"}})

# Dictionary to store user balances
user_balances = {}

class MoneyAPI:
    class User(Resource):
        def get(self, current_user, user_id):
            if current_user['_uid'] != user_id:
                return jsonify({"error": "Unauthorized"}), 401
            
            balance = user_balances.get(user_id)
            if balance is not None:
                return jsonify({user_id: balance})
            else:
                return jsonify({"error": "User not found"}), 404


api.add_resource(MoneyAPI.User, '/user/<string:user_id>')

if __name__ == "__main__":
    server = "http://127.0.0.1:8987" # run local
    # server = 'https://chat.stu.nighthawkcodingsociety.com'  # Update with your server URL
    url = server + "/api/money"
    responses = []
