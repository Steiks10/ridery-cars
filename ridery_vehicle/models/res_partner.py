from odoo import models, fields, api, _
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

    def send_partner_vehicles_to_an_api(self):
        self.ensure_one()
        request_service = self.env['request.abstract.service']
        vehicles = self.env['fleet.vehicle'].search([('driver_id', '=', self.id)])
        vehicles_data = []
        for vehicle in vehicles:
            vehicles_data.append({
                'id': vehicle.id,
                'name': vehicle.name,
                'license_plate': vehicle.license_plate,
                'model_id': vehicle.model_id.name,
                'stock_id': vehicle.stock_location_id.name,
                'company_id': vehicle.company_id.name,
            })
        url = 'http://localhost:3000/vehicles'
        headers = {'Content-Type': 'application/json'}
        try:
            response = request_service.send_request_to_app(url, method='POST', data=vehicles_data, headers=headers)
            if response.status_code in (200, 201):
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('¡Exitoso!'),
                        'message': _('Los vehículos han sido enviados correctamente.'),
                        'type': 'success',
                        'sticky': False,
                    }
                }
            else:
                # Respuesta pero no exitosa
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Error'),
                        'message': _('El servidor respondió con error: %s' % response.text),
                        'type': 'danger',
                        'sticky': True,
                    }
                }
        except Exception as e:
            # Error de conexión, etc
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Error de conexión'),
                    'message': _('No se pudo enviar los datos: %s' % str(e)),
                    'type': 'danger',
                    'sticky': True,
                }
            }
