from flask import Blueprint
from app.api.v1 import account

def create_blueprint_v1():

    blueprint_v1 = Blueprint('v1', __name__)

    account.api.register(blueprint_v1)

    return blueprint_v1
