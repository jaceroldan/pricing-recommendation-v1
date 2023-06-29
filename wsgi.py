import os
import sys
from app import app, BASE_PATH


def start_app():
    [sys.path.append(os.path.join(os.getcwd(), path))
        for path in ['routes', 'utils']]

    from routes import root, pricing_recommendation as pr

    app.register_blueprint(root.root, url_prefix=BASE_PATH)
    app.register_blueprint(pr.pricing_recommendation, url_prefix=BASE_PATH)


start_app()
