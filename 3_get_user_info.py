# Vulnerability Type: (CWE-639) Authorization Bypass Through User-Controlled Key
# Severity: High

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database of user information
users = {
    'alice': {'id': 1, 'name': 'Alice', 'balance': 1000, 'email' : 'alice@example.io', 'authToken' : 'YWxpY2VfYXV0aFRva2VuX2FiNzljNw=='},
    'bob': {'id': 2, 'name': 'Bob', 'balance': 500, 'email' : 'bob@example.io', 'authToken' : 'Ym9iX2F1dGhUb2tlbl9mZjBkYzc='},
    'charlie': {'id': 3, 'name': 'Charlie', 'balance': 200, 'email' : 'charlie@example.io', 'authToken' : 'Y2hhcmxpZV9hdXRoVG9rZW5fYTA5OGRh'}
}

# Endpoint to fetch user information
@app.route('/user', methods=['GET'])
def get_user_info():
    user_id = request.args.get('id')

    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(users[user_id]), 200

if __name__ == '__main__':
    app.run(debug=True)