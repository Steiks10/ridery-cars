from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   app_vehicle_secret = fields.Char(string="Secret Key", related='company_id.app_vehicle_secret', readonly=False)
