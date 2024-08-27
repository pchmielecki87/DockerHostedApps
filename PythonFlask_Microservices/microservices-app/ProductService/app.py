from flask import Flask, jsonify

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
    app.run(host='0.0.0.0', port=5012)
