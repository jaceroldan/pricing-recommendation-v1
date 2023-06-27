from decimal import Decimal
from flask import Blueprint, request
from pricing_model_utils.xgb import xgb_predict
from pricing_model_utils.lgb import lgb_predict

pricing_recommendation = Blueprint('pricing_recommendation', __name__)


@pricing_recommendation.route('/pricing-recommendation-xgb')
def get_xgb_pricing_recommendation():
    
    args = dict(request.args)
    result = float(str(xgb_predict(args)))

    return {'message': 'ok', 'result': result}

@pricing_recommendation.route('/pricing-recommendation-lgb')
def get_lgb_pricing_recommendation():
    args = dict(request.args)
    result = float(str(lgb_predict(args)))

    return {'message': 'ok', 'result': result}
