from odoo import models, fields


class Property(models.Model):
    _name = 'property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property'

    name = fields.Char(string="Property's Name")
    adresse = fields.Char(string="Adresse")
    rent_mount = fields.Integer(string="Rent Mount")
    owner_id = fields.Many2one('owner', string='The Owner')
    note = fields.Text(string='Note')
    property_type = fields.Selection([
        ('appartment', 'Appartment'),
        ('house', 'House'), ('commercial', 'Commercial'), ('personal_property', 'Personal property'),
        ('intangible_property', 'Intangible property')
    ], default='personal_property', string="Property type")
    location = fields.Char(string='Location')
    tenant_id = fields.Many2one('tenant', string='Tenant')
    state = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance'),
    ], string='Status', readonly=True, default='available')

    """ open a wizard for defining the reason of maintenance"""

    def action_open_maintenance_wizard(self):

        return {
            'name': 'maintenance',
            'type': 'ir.actions.act_window',
            'res_model': 'maintenance.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_note': self.note},
        }

    def action_available(self):
        self.state = 'available'

    def action_rented(self):
        self.state = 'rented'

    def action_maintenance(self):
        self.state = 'maintenance'
