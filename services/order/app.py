from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

orders = []  # list of orders

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders), 200

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    order = {
        "id": len(orders) + 1,
        "user_id": data.get("user_id"),
        "products": data.get("products"),
        "total": data.get("total"),
        "date": datetime.utcnow().isoformat()
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
