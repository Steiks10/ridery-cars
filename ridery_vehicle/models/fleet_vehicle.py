from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    stock_location_id = fields.Many2one(
        'stock.location',
        string='Stock Location',
        help='Stock location of the car'
    )
    sequence = fields.Char(string="Sequence")
    vehicle_image = fields.Binary(string="Vehicle Image")

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].sudo().next_by_code('sequence_ridery_vehicle')
        return super(FleetVehicle, self).create(vals)