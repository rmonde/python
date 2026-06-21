from flask import Blueprint

orders_bp = Blueprint('orders',__name__)

@orders_bp.route('/', methods=['GET'])
def list_orders():
    return {"orders": ["ord-001", "ord-002"]}