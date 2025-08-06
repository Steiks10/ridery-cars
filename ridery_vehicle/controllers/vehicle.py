import odoo
from odoo import http, _
from odoo import fields
from odoo.http import request, Response
import hmac
from datetime import datetime, timedelta, date
import random
import logging
import json
from .middleware import middleware_ridery_decorator

_logger = logging.getLogger(__name__)
class ElearningController(http.Controller):
    @http.route('/ridery/vehicle', auth='public', methods=['POST'], type='http', csrf=False)
    @middleware_ridery_decorator
    def create_vehicle(self, **kwargs):
        http_method = request.httprequest.method
        helper = request.env['response.helper']
        ridery_logger = request.env['ridery.log'].sudo()
        try:
            data = request.httprequest.get_data()
            request_values = json.loads(data.decode('utf-8'))

            stock_location_id = False
            state_id = request.env['fleet.vehicle.state'].sudo().search([('name', '=', request_values.get('state_id'))])
            model_id = request.env['fleet.vehicle.model'].sudo().search([('name', '=', request_values.get('model_id'))])
            driver_id = request.env['res.partner'].sudo().search([('vat', '=', request_values.get('driver_id'))])
            model_year = request_values.get('model_year')
            color = request_values.get('color')
            license_plate = request_values.get('license_plate')
            if request_values.get('stock_location_id'):
                stock_location_id = request.env['res.partner'].sudo().search([('name', '=', request_values.get('stock_location_id'))])
            vehicle_created = self.create_fleet_vehicle(
                state_id,
                model_id,
                driver_id,
                model_year,
                color,
                license_plate,
                stock_location_id
            )
            vehicle_created_response_data = {'id': vehicle_created.id}
            return helper.success_response(vehicle_created_response_data)
        except Exception as e:
            _logger.error("Invoice creation error: %s", str(e))
            response_text = str(e)
            return helper.error_response(response_text, 500)

    def create_fleet_vehicle(self, state_id, model_id, driver_id, model_year, color, license_plate, stock_location_id=False):
        return request.env['fleet.vehicle'].sudo().create({
            'state_id': state_id.id,
            'model_id': model_id.id,
            'driver_id': driver_id.id,
            'model_year': model_year,
            'color': color,
            'license_plate': license_plate,
            'stock_location_id': stock_location_id.id,
        })




