from decimal import Decimal
from flask import Blueprint, request, jsonify as json
from pricing_model_utils.xgb import xgb_predict
from pricing_model_utils.lgb import lgb_predict
from util.util import query
from marshmallow import Schema, fields, validate, ValidationError


class CarDetailsSchema(Schema):
    # will add defaults later
    color = fields.String(required=True)
    number_of_seats = fields.Integer(required=True)
    number_of_doors = fields.Integer(required=True)
    type_of_gas = fields.String(validate=validate.OneOf(['gas', 'diesel']))
    kilometers_per_liter = fields.Integer(required=True)
    mileage = fields.String(required=True)


pricing_recommendation = Blueprint('pricing_recommendation', __name__)


schema = CarDetailsSchema()


@pricing_recommendation.route('/pricing-recommendation-xgb')
def get_xgb_pricing_recommendation():
    try:
        args = dict(request.args)
        data = query("""
        SELECT color, number_of_seats, number_of_doors, type_of_gas, 
        kilometers_per_liter, mileage from dashboard.car_inventory
        WHERE color = %(color)s AND number_of_seats = %(number_of_seats)s
        AND number_of_doors = %(number_of_doors)s AND type_of_gas = %(type_of_gas)s
        AND kilometers_per_liter = %(kilometers_per_liter)s AND mileage = %(mileage)s;   
        """, args)

        result = float(str(xgb_predict(args)))

        return {'message': 'ok', 'result': result}
    except ValidationError as e:
        print(e)
        return json({'message': str(e)}), 400
    except Exception as e:
        print(e)
        return json({'message': str(e)}), 500


@pricing_recommendation.route('/pricing-recommendation-lgb')
def get_lgb_pricing_recommendation():
    args = dict(request.args)

    try:
        schema.load(args)

        data = query("""
        SELECT color, number_of_seats, number_of_doors, type_of_gas, 
        kilometers_per_liter, mileage from dashboard.car_inventory
        WHERE color = %(color)s AND number_of_seats = %(number_of_seats)s
        AND number_of_doors = %(number_of_doors)s AND type_of_gas = %(type_of_gas)s
        AND kilometers_per_liter = %(kilometers_per_liter)s AND mileage = %(mileage)s;   
        """, args)

        result = float(str(lgb_predict(args)))

        return {'message': 'ok', 'result': result}
    except ValidationError as e:
        print(e)
        return json({'message': str(e)}), 400
    except Exception as e:
        print(e)
        return json({'message': str(e)}), 500
