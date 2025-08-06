import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/handle_kite_event', methods=['GET', 'POST'])
def handle_kite_event():
    data = request.args.to_dict() if request.method == 'GET' else request.form.to_dict()
    print("Received from Render:", data)
    return jsonify({"status": "received by local app"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)