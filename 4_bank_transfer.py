# Vulnerability Type: (CWE-1284) Improper Validation of Specified Quantity in Input
# Severity: Medium

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database of user account balances
user_accounts = {
    'alice': 1000,
    'bob': 500,
    'charlie': 200
}

# Endpoint to transfer funds from one account to another
@app.route('/transfer', methods=['POST'])
def transfer_funds():
    data = request.get_json()
    sender = data.get('sender')
    recipient = data.get('recipient')
    amount = data.get('amount')

    if sender not in user_accounts or recipient not in user_accounts or sender == recipient:
        return jsonify({'error': 'Invalid sender or recipient'}), 400

    if user_accounts[sender] < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    user_accounts[sender] -= amount
    user_accounts[recipient] += amount

    return jsonify({'message': 'Transfer successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)