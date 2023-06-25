from flask import Flask
from config import config
import os

app = Flask(__name__)

BASE_PATH = '/api'


def start_app():
    # was having import problems, working with python imports is a bit different in js/nodejs
    [os.path.join(os.getcwd(), path) for path in ['routes', 'utils']]

    from routes import root, pricing_recommendation as pr

    app.register_blueprint(root.root, url_prefix=BASE_PATH)
    app.register_blueprint(pr.pricing_recommendation, url_prefix=BASE_PATH)

    app.run(port=config.PORT, debug=config.DEBUG)


if __name__ == '__main__':
    start_app()
