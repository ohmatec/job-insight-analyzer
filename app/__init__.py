from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  # โหลด .env
    app = Flask(__name__)
    app.config['RAPIDAPI_KEY'] = os.getenv('RAPIDAPI_KEY')
    app.config['RAPIDAPI_HOST'] = os.getenv('RAPIDAPI_HOST')

    from .routes import main
    app.register_blueprint(main)
    return app
