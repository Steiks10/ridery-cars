from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    stock_location_id = fields.Many2one(
        'stock.location',
        string='Ubicación de Inventario',
        help='Ubicación de stock asociada al vehículo'
    )