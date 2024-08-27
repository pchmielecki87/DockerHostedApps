import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

USER_SERVICE_URL = 'http://user-service:5001'
PRODUCT_SERVICE_URL = 'http://product-service:5002'

@app.route('/orders', methods=['POST'])
def create_order():
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    
    user = requests.get(f'{USER_SERVICE_URL}/users/{user_id}').json()
    product = requests.get(f'{PRODUCT_SERVICE_URL}/products/{product_id}').json()
    
    if not user or not product:
        return "Invalid user or product", 400
    
    order = {"id": len(orders) + 1, "user": user, "product": product}
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013)
