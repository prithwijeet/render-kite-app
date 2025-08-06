from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/handle_kite_event', methods=['POST'])
def handle_kite_event():
    data = request.json
    print("Received from Render:", data)
    return jsonify({"status": "received by local app"})

if __name__ == '__main__':
    app.run(port=5001)