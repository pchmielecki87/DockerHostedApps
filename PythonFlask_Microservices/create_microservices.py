import os

# Define the services and their files
services = {
    "UserService": {
        "app.py": """from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
""",
        "requirements.txt": "flask",
        "Dockerfile": """FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
"""
    },
    "ProductService": {
        "app.py": """from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Product 1"},
    {"id": 2, "name": "Product 2"},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else ("Product not found", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
""",
        "requirements.txt": "flask",
        "Dockerfile": """FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]
"""
    },
    "OrderService": {
        "app.py": """import requests
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
    app.run(host='0.0.0.0', port=5003)
""",
        "requirements.txt": "flask requests",
        "Dockerfile": """FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

CMD ["python", "app.py"]
"""
    }
}

# Create the directory structure and files
base_dir = "microservices-app"

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

for service, files in services.items():
    service_dir = os.path.join(base_dir, service)
    os.mkdir(service_dir)
    for filename, content in files.items():
        with open(os.path.join(service_dir, filename), 'w') as f:
            f.write(content)

print("Microservices application structure created successfully.")
