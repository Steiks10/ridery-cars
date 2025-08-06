from odoo import http
from functools import wraps
from odoo.http import request, Response
import json
from werkzeug.exceptions import Unauthorized


def middleware_ridery_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        req = request.httprequest
        ridery_logger = request.env['ridery.log'].sudo()
        http_method = req.method

        def log_and_raise(status, text):
            helper = request.env['response.helper']
            ridery_logger.create({'status': status, 'method': http_method, 'response_text': text})
            return helper.error_response(text, status)

        # Validación de Authorizationd
        auth_header = req.headers.get('Authorization')
        if not auth_header:
            return log_and_raise(401, "Authorization header is missing")

        # Validación de Company
        company_names = req.headers.get('X-Company-Name')
        name_list = [name.strip() for name in company_names.split(',')] if company_names else []
        company_objects = request.env['res.company'].sudo().search([('name', 'in', name_list)])
        if not company_objects:
            return log_and_raise(401, "Not match with company")

        # Validación de secreto
        if not any(company.app_vehicle_secret == auth_header for company in company_objects):
            return log_and_raise(401, "auth header didn`t match with company`s api secret")

        # Ejecución de la función original
        response = func(*args, **kwargs)

        # Extracción de información para el log
        status = getattr(response, 'status_code', 200)
        if isinstance(response, dict) and 'status' in response:
            status = response['status']
        response_text = str(response) if isinstance(response, (str, bytes)) else getattr(response, 'data', str(response))

        ridery_logger.create({'status': status, 'method': http_method, 'response_text': response_text})
        return response

    return wrapper