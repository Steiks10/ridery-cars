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

"""
Módulo: vehicle.py
-------------------
Este controlador gestiona la creación de vehículos en Odoo 16 a través de una ruta HTTP POST (`/ridery/vehicle`).
Utiliza el decorador de middleware para validaciones y permite registrar vehículos desde una integración externa (por ejemplo, una app web).

- Endpoint principal: `/ridery/vehicle` (POST)
- Permite crear vehículos en el módulo Fleet usando datos enviados por terceros.
- Realiza búsquedas y validaciones de datos relacionados (estado, modelo, conductor, ubicación).
- Responde con el ID del vehículo creado o un error detallado.

Autor: Ridery Team
"""
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
        helper = request.env['response.helper']
        try:
            request_values = json.loads(request.httprequest.get_data().decode('utf-8'))

            search_map = {
                'state_id': ('fleet.vehicle.state', 'name'),
                'model_id': ('fleet.vehicle.model', 'name'),
                'driver_id': ('res.partner', 'vat'),
                'stock_location_id': ('stock.location', 'name'),
            }
            resolved = {}
            for key, (model, field) in search_map.items():
                value = request_values.get(key)
                if value:
                    resolved[key] = request.env[model].sudo().search([(field, '=', value)], limit=1)
                else:
                    resolved[key] = False
            vehicle_vals = {
                'state_id': resolved['state_id'].id if resolved['state_id'] else False,
                'model_id': resolved['model_id'].id if resolved['model_id'] else False,
                'driver_id': resolved['driver_id'].id if resolved['driver_id'] else False,
                'model_year': request_values.get('model_year'),
                'color': request_values.get('color'),
                'license_plate': request_values.get('license_plate'),
                'stock_location_id': resolved['stock_location_id'].id if resolved['stock_location_id'] else False,
                'company_id': resolved['stock_location_id'].company_id.id
            }

            # Create the vehicle
            vehicle_created = request.env['fleet.vehicle'].sudo().create(vehicle_vals)
            return helper.success_response({'id': vehicle_created.id})

        except Exception as e:
            _logger.error("Vehicle creation error: %s", str(e))
            return helper.error_response(str(e), 500)
