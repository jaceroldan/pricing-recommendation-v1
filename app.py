from flask import Flask
from config import config
from util import query

app = Flask(__name__)


@app.route('/')
def root():
    return {'statusCode': 200, 'message': 'Hello World!'}


@app.route('/test')
def test():

    try:
        return query('SELECT * FROM dashboard.car_inventory ORDER BY id ASC LIMIT 10')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(port=config.PORT, debug=config.DEBUG)
