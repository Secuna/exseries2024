from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.isAdmin = False

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, password={self.password}, isAdmin={self.isAdmin})"

@app.route('/create_user', methods=['POST'])
def create_user():
    global users
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        new_user = User()
        for key, value in data.items():
            setattr(new_user, key, value)

        users.append(new_user)
        return jsonify({"message": "User created successfully", "user": new_user.__dict__}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)