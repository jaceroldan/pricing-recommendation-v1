from util.util import query
from flask import Blueprint


pricing_recommendation = Blueprint('pricing_recommendation', __name__)


@pricing_recommendation.route('/pricing_recommendation')
def get_pricing_recommendation():
    result = query(
        'SELECT * FROM dashboard.car_inventory ORDER BY id ASC LIMIT 10')
    return {'message': 'ok', 'result': result}
