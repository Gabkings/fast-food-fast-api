from flask import Flask
from flask_restful import Api
from config import app_config
from .orders import OrderDetals,DisplayAllOrders
#from .users import DisplayAllUsers,UserCreation,UserDetails
def create_app(config_stage):
    Gabriel = Flask(__name__)
    app.config.from_object(app_config[config_stage])
    api = Api(app)
    '''Versioning of the endpoints url'''
    api.add_resource(DisplayAllOrders, '/api/v1/orders')
    return Gabriel
