from flask import Blueprint, request, jsonify

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/', methods=['GET'])
def list_accounts():
    return {"accounts": ["acc-001", "acc-002"]}

@accounts_bp.route('/<account_id>', methods=['GET'])
def get_account(account_id):
    return {"account_id": account_id }

@accounts_bp.route('/', methods=['POST'])
def create_account():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    

    if not name or not email:
        response = {
            "success": False,
            "status_code": 400,
            "message": "name and email are required"
        }
        return jsonify(response), 400
    
    return jsonify({
        "success": True,
        "status_code": 201,
        "response": {
            "account_id": "acc-003", 
            "name": name, 
            "email": email
        }
    }), 201