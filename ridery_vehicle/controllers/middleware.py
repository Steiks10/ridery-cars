from odoo import http
from odoo.http import request
from functools import wraps
from odoo.http import request, Response
import json
from werkzeug.exceptions import Unauthorized


def middleware_ridery_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.httprequest.headers.get('Authorization')
        if not auth_header:
            raise Unauthorized(description="Authorization header is missing")
        company_names = request.httprequest.headers.get('X-Company-Name')
        name_list = [name.strip() for name in company_names.split(',')]
        company_objects = request.env['res.company'].sudo().search([('name', 'in', name_list)])
        if not company_objects:
            raise Unauthorized(description="Not match with company")
        if not any(company.app_vehicle_secret == auth_header for company in company_objects):
            raise Unauthorized(description="auth header didn`t match with company`s api secret")
        response = func(*args, **kwargs)
        http_method = request.httprequest.method
        # Serializa la respuesta para el log (puedes adaptarlo según tu helper)
        response_text = str(response) if isinstance(response, (str, bytes)) else getattr(response, 'data',
                                                                                            str(response))
        if hasattr(response, 'status_code'):
            status = response.status_code
        elif isinstance(response, dict) and 'status' in response:
            status = response['status']
        else:
            status = 200
        # Registra el log
        ridery_logger = request.env['ridery.log'].sudo()
        ridery_logger.create({
            'status': status,
            'method': http_method,
            'response_text': response_text
        })
        return response
    return wrapper