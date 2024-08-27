import os

# Define the directory structure and files with their content
project_structure = {
    "UserService": {
        "app.py": """\
from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
""",
        "requirements.txt": "Flask==2.3.2",
        "Dockerfile": """\
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
"""
    },
    "ProductService": {
        "app.py": """\
from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
""",
        "requirements.txt": "Flask==2.3.2",
        "Dockerfile": """\
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]
"""
    }
}

# Function to create directories and files
def create_project_structure(base_path, structure):
    for directory, files in structure.items():
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        for file_name, file_content in files.items():
            with open(os.path.join(dir_path, file_name), 'w') as file:
                file.write(file_content)
                print(f"Created {os.path.join(dir_path, file_name)}")

# Set the base path and create the project structure
base_path = os.path.abspath("soa-app")
create_project_structure(base_path, project_structure)

print(f"\nSOA project structure created successfully in {base_path}")
