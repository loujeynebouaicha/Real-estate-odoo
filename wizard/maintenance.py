from odoo import fields, models


class Maintenance(models.TransientModel):
    _name = 'maintenance.wizard'

    note = fields.Text(string='Description for The Maintenance')

