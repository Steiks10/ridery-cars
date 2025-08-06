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
        print()
        helper = request.env['response.helper']
        try:
            data = request.httprequest.get_data()
            request_values = json.loads(data.decode('utf-8'))
            return helper.success_response({'id': 1})
        except Exception as e:
            _logger.error("Invoice creation error: %s", str(e))
            return helper.error_response(str(e), 500)




