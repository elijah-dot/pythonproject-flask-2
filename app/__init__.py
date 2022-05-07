#import of esentials
from flask import Flask




def create_app(config_name):
    app = Flask(__name__)
    #import of blue prints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
