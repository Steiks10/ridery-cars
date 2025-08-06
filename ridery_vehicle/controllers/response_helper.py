from odoo import models, fields, api, _
from odoo.http import request, Response
from datetime import datetime
import json

# Helper para estandarizar las respuestas de la API externa
class ResponseHelper(models.AbstractModel):
    _name = 'response.helper'
    _description = 'Response helper'

    def error_response(self, message, status_code):
        # Respuesta de error en formato JSON
        return Response(
            json.dumps({'error': message}),
            content_type='application/json;charset=utf-8',
            status=status_code
        )

    def success_response(self, data, status=200):
        # Respuesta exitosa en formato JSON
        return Response(
            json.dumps(data),
            content_type='application/json;charset=utf-8',
            status=status
        )