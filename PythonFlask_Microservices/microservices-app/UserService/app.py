from flask import Flask, jsonify

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
    app.run(host='0.0.0.0', port=5011)
