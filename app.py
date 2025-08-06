import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LOCAL_APP_URL = "https://7450c8a3386e.ngrok-free.app/handle_kite_event"  # Your local app endpoint

@app.route('/')
def index():
    return 'Render Kite Test App is running!'

@app.route('/callback', methods=['GET', 'POST'])
def callback():
    print("Received /callback request")
    data = request.args.to_dict() if request.method == 'GET' else request.form.to_dict()
    print("Callback Data:", data)

    # Remove or comment out the forwarding for now
    return jsonify({
        "status": "received",
        "forwarded_to_local": False,
        "received_data": data
    })

@app.route('/postback', methods=['POST'])
def postback():
    data = request.json or request.form.to_dict()
    print("Postback Data:", data)

    try:
        requests.post(LOCAL_APP_URL, json={"source": "kite_postback", "data": data})
    except Exception as e:
        print("Could not forward to local app:", e)

    return jsonify({"status": "received", "forwarded_to_local": True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)
