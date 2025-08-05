from odoo import models, fields, api, _
import requests


class RequestAbstractService(models.AbstractModel):
    _name = 'request.abstract.service'
    _description = 'Request Abstract Service'

    def send_request_to_app(self, url, method='GET', data=None, headers=None, timeout=10):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method.upper() == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=timeout)
            elif method.upper() == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=timeout)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=timeout)
            else:
                raise ValueError("Método HTTP no soportado: %s" % method)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise Exception(f'Error en request HTTP: {e}')