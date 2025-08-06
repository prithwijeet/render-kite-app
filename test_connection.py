import requests

RENDER_BASE_URL = "https://render-kite-app.onrender.com"

# Sample GET /callback request
def test_get_callback():
    params = {
        "event": "login_success",
        "user_id": "AB1234"
    }
    response = requests.get(f"{RENDER_BASE_URL}/callback", params=params)
    print("GET /callback response:", response.json())

# Sample POST /callback request (form-data)
def test_post_callback():
    data = {
        "event": "order_placed",
        "order_id": "XYZ5678"
    }
    response = requests.post(f"{RENDER_BASE_URL}/callback", data=data)
    print("POST /callback response:", response.json())

# Sample POST /postback request (JSON)
def test_post_postback():
    payload = {
        "event": "order_filled",
        "order_id": "ORD123456",
        "status": "complete"
    }
    response = requests.post(f"{RENDER_BASE_URL}/postback", json=payload)
    print("POST /postback response:", response.json())

# --- Run all three tests
if __name__ == "__main__":
    test_get_callback()
    test_post_callback()
    test_post_postback()