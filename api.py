from flask import Blueprint, jsonify, request
from service import *

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/add_product', methods=['POST'])                              #Add new product
def api_add_product():
    product_data = request.get_json()  
    result= add_product(product_data)
    if result:
        return jsonify({"message": "Product created successfully"})

@api_bp.route('/api/products', methods=['GET'])                                  #List all products
def api_products():
    products = get_all_products()
    products_data = [product.to_dict() for product in products]    #content of products is object
    return jsonify(products_data)

@api_bp.route('/api/product/<product_name>', methods=['GET'])                    #List product by name
def api_product_detail(product_name):
    product = get_products_by_name(product_name)
    if product:
        products_data = [product.to_dict() for product in product]
        return jsonify(products_data)
    return jsonify({"error": "Product not found"})

@api_bp.route('/api/product/<product_name>/stock', methods=['PUT'])              #Update stock
def api_update_product_stock(product_name):
    result= update_product_stock(product_name)
    if result:
        return jsonify({"message": "Product stock updated successfully"})
    else:
        return jsonify({"message": "Product stock not updated"})
    
@api_bp.route('/api/product/<product_name>', methods=['DELETE'])                #Delete product
def api_delete_product(product_name):
    product = get_products_by_name(product_name)
    if product:
        result=delete_product(product_name)
        return jsonify({"message": "Product deleted successfully"})
    else:
        return jsonify({"message": "Product not found"})
    

@api_bp.route('/api/add_user', methods=['POST'])                              #Add new user
def api_add_user():
    user_data = request.get_json()  
    result= add_user(user_data)
    if result:
        return jsonify({"message": "User created successfully"})

@api_bp.route('/api/users', methods=['GET'])                                     #List all users
def api_users():
    users = get_all_users()
    users_data = [
        {"username": u.username, "email": u.email}
        for u in users
    ]
    return jsonify(users_data)

@api_bp.route('/api/user/<username>', methods=['GET'])                           #List user by name
def api_user_detail(username):
    user = get_user_by_username(username)
    if user:
        user_data = {
            "username": user.username,
            "email": user.email
        }
        return jsonify(user_data)
    return jsonify({"error": "User not found"})
