from flask import Blueprint


root = Blueprint('root', __name__)


@root.route('/')
def root_route():
    return {'statusCode': 200, 'message': 'Hello World!'}
