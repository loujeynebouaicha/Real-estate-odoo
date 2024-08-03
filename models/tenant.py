from odoo import models, fields


class Tenant(models.Model):
    _name = 'tenant'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tenants'

    name = fields.Many2one('res.partner', string="Name")
    mail = fields.Char(related='name.email', string="Mail")
    phone = fields.Char(related='name.phone', string="Phone")
    property_ids = fields.One2many('property', 'tenant_id', string='Available Properties',
                                   domain=[('state', '=', 'available')])