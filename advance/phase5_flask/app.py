from flask import Flask, jsonify, request
from routes import accounts
from routes import orders


# Create the flask app, register both blueprints

app = Flask(__name__)

app.register_blueprint(accounts.accounts_bp, url_prefix='/accounts')
app.register_blueprint(orders.orders_bp, url_prefix='/orders')

@app.errorhandler(404)
def not_found(error):
    response = {
        "success": False,
        "status_code": 403,
        "message": "Resource not found"
    }
    return jsonify(response), 404

@app.errorhandler(405)
def method_not_allowed(error):
    response = {
        "success": False,
        "status_code": 405,
        "message": "The HTTP method is not allowed for this endpoint"
    }

    return jsonify(response), 405

@app.before_request
def log_request():
    print(f"Incoming: {request.method} {request.path}")

@app.after_request
def add_header(response):
    # after_request MUST return the response object
    response.headers["X-Powered-By"]= "Rahul-API"
    return response

if __name__=="__main__":
    app.run(debug=True)
  