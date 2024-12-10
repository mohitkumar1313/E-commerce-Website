from flask import Flask
from api import api_bp
from database import insert_static_data  # Import the function to insert static data
from flasgger import Swagger

app = Flask(__name__)

# Insert static data into the database
insert_static_data()

#swagger = Swagger(app)
swagger = Swagger(app, template_file='swagger.yml')


# Register the Blueprint with the Flask app
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
