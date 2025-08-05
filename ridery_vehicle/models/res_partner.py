from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def partner_vehicles_smart_button(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Partner Vehicles',
            'view_mode': 'kanban,tree',
            'res_model': 'fleet.vehicle',
            "context": {"create": False},
            'domain': [('driver_id', '=', self.id)],
        }

    def _get_ridery_driver_view(self):
        user_ids = list(set(self.env['fleet.vehicle'].search([('driver_id', '!=', False)]).mapped('driver_id.id')))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Drivers',
            'view_mode': 'kanban,tree,form',
            'res_model': 'res.partner',
            "context": {"create": False},
            'domain': [('id', 'in', user_ids)],
        }

