from model import Product, User
from database import get_db


def add_product(product_data):  # Add a new product
    db = get_db()
    products_collection = db['products']
    products_collection.insert_one(product_data)

def get_all_products():     #List all the products in Database
    db = get_db()
    products_collection = db['products']
    products_data = list(products_collection.find()) 
    products = [Product(product['name'], product['description'], product['price'], product['stock']) for product in products_data]
    return products

def get_products_by_name(product_name):    
    db = get_db()
    products_collection = db['products']
    products_cursor = products_collection.find({"name": product_name})  # Cursor for multiple products
    products_data = list(products_cursor)  # Convert cursor to list

    # Convert each product dictionary to a Product object
    products = [Product(
                    product['name'],
                    product['description'],
                    product['price'],
                    product['stock']
                ) for product in products_data]

    return products



def update_product_stock(product_name):  # Update product stock
    db = get_db()
    products_collection = db['products']
    product_data= products_collection.update_one({"name": product_name}, {"$set": {"stock": 5}})
    if product_data:
        return True
    
def delete_product(product_name):  # Delete a product
    db = get_db()
    products_collection = db['products']
    product_data= products_collection.delete_one({"name": product_name})
    if product_data:
        return True


def get_all_users():        #List all the users in Database
    db = get_db()
    users_collection = db['users']
    users_data = list(users_collection.find())  # Fetch all users from the database
    users = [User(u['username'], u['email'], u['password']) for u in users_data]
    return users

def get_user_by_username(username):
    db = get_db()
    users_collection = db['users']
    user_data = users_collection.find_one({"username": username})  # Find user by username
    if user_data:
        return User(user_data['username'], user_data['email'], user_data['password'])
    return None


# def delete_user(username):  # Delete a product
#     db = get_db()
#     user= db['users']
#     user_data= user.delete_one({"name": username})
#     if user_data:
#         return True