from flask import Flask, jsonify

app = Flask(__name__)

# Sample data - normally this would come from a database
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Headphones", "price": 149.99}
]

# Routes
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "API is running",
        "endpoints": ["/users", "/products", "/users/<id>", "/products/<id>"]
    })

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "count": len(users),
        "data": users
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify({
            "status": "success",
            "data": user
        })
    return jsonify({
        "status": "error",
        "message": "User not found"
    }), 404

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({
        "status": "success",
        "count": len(products),
        "data": products
    })

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify({
            "status": "success",
            "data": product
        })
    return jsonify({
        "status": "error",
        "message": "Product not found"
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)