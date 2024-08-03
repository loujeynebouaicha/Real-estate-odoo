from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Owners'

    name = fields.Many2one('res.partner', string="Name")
    mail = fields.Char(related='name.email', string="Mail")
    phone = fields.Char(related='name.phone', string="Phone")
    property_id = fields.One2many('property','owner_id', string='Properties')
    properties_count = fields.Integer(string='Properties Count', compute='compute_properties_count')
    state = fields.Char()

    """methode de count properties of owner"""

    def compute_properties_count(self, _logger=None):
        for record in self:
            try:
                record.properties_count = self.env['property'].search_count([('owner_id', '=', record.id)])
            except Exception as e:
                record.properties_count = 0
                _logger.error(f"Failed to compute properties_count for owner {record.id}: {str(e)}")

    def action_property(self):
        return {
            'type': 'ir.actions.act_window',
            'name': ('Properties'),
            'domain': [('owner_id', '=', self.id)],
            'res_model': 'property',
            'view_mode': 'tree,form',
            'target': 'current',
        }

