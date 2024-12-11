class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

class Product:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock
        }
