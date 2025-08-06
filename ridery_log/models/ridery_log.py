from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta

# Modelo principal para registrar logs de integración con terceros
class RideryLog(models.Model):
    _name = "ridery.log"
    _description = "Ridery Log"

    status = fields.Char(string="Status")
    response_text = fields.Text(string="Response Text")
    method = fields.Char(string='Method')
