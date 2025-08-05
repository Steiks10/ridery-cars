from odoo import models, fields, api

class ResCompany(models.Model):
   _inherit = 'res.company'
   _description = 'Company'

   app_vehicle_secret = fields.Float('Unit Credit')