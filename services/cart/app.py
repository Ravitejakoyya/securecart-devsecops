from flask import Flask, jsonify, request

app = Flask(__name__)

carts = {}  # user_id -> list of product ids

@app.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    cart = carts.get(user_id, [])
    return jsonify({"user_id": user_id, "products": cart}), 200

@app.route("/cart/<int:user_id>", methods=["POST"])
def add_to_cart(user_id):
    product_id = request.json.get("product_id")
    if user_id not in carts:
        carts[user_id] = []
    carts[user_id].append(product_id)
    return jsonify({"user_id": user_id, "products": carts[user_id]}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
