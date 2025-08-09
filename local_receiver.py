import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/handle_kite_event', methods=['GET', 'POST'])
def handle_kite_event():
    if request.is_json:
        data = request.get_json()
    elif request.method == 'POST':
        data = request.form.to_dict()
    else:
        data = request.args.to_dict()

    print("📥 Received from Render:", data)
    return jsonify({"status": "received by local app"})

@app.route('/redirect')
def oauth_redirect():
    code = request.args.get('code')
    print("Received code:", code)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)