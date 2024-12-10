from flask import Flask
from api import api_bp
from database import insert_static_data  # Import the function to insert static data

app = Flask(__name__)

# Insert static data into the database
insert_static_data()

# Register the Blueprint with the Flask app
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
