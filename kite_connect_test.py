from kiteconnect import KiteConnect, KiteTicker
from flask import Flask, request, jsonify
import webbrowser

# Fill in your credentials
API_KEY = "ylj4lqzbja6unjrl"
API_SECRET = "i9acfiiu05ilui2wyhbgejje7mfsbpgf"
REDIRECT_URL = "http://localhost:5000/redirect"  # or your ngrok/render redirect URL

kite = KiteConnect(api_key=API_KEY)
app = Flask(__name__)
access_token = "BQFYYO5ea4721m2Oz2khezwtEjOAnZoK"


@app.route("/")
def login():
    login_url = kite.login_url()
    print("Login at:", login_url)
    webbrowser.open(login_url)  # opens browser automatically
    return f"Go to this URL to login: <a href='{login_url}' target='_blank'>{login_url}</a>"

@app.route("/instruments")
def get_instruments():
    kite.set_access_token(access_token)
    instruments = kite.margins()
    print(instruments)
    return jsonify(instruments)

@app.route("/redirect")
def redirect_handler():
    global access_token
    request_token = request.args.get("request_token")
    # print("Received request_token:", request_token)

    try:
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        access_token = data["access_token"]
        print("Access token:", access_token)

        kite.set_access_token(access_token)
        print("Logged in successfully!")
        return jsonify({
            "status": "Login successful"
        })
        # profile = kite.profile()
        # print("Your Profile Info:", profile)
        # return jsonify({
        #     "status": "Login successful",
        #     "access_token": access_token,
        #     "profile": profile
        # })

    except Exception as e:
        print("Login failed:", e)
        return f"Login failed: {e}", 500


if __name__ == "__main__":
    app.run(port=5000)
