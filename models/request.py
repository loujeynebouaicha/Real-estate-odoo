from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Request(models.Model):
    _name = 'request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Requests'

    name = fields.Char(string="Name")
    sequence = fields.Char(string='Request Number', required=True, copy=False, readonly=True, default='New')
    mail = fields.Char(string='Email')
    phone = fields.Integer(string='Phone Number')
    date_debut = fields.Date(string='Start Date')
    date_fin = fields.Date(string='End Date')
    tenant_id = fields.Many2one('tenant', string='The tenant')
    property_id = fields.Many2one('property', string='Related Property', ondelete='cascade')
    mount = fields.Integer(related ='property_id.rent_mount', string='Rent Mount')
    mount_prop = fields.Integer(string='Mount Proposed')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('send_email', 'Sent to Owner'),
        ('confirm', 'Confirm'),
        ('refuse', 'Refuse'),
    ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        self.state = 'confirm'
        template = self.env.ref('real_estate_app.email_template_real_estate_notification_owner_confirm')
        for rec in self:
            template.send_mail(rec.id, force_send=True)

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('request.sequence') or 'New'
        return super(Request, self).create(vals)

    def action_draft(self):
        self.state = 'draft'

    def action_refuse(self):
        self.state = 'refuse'
        template = self.env.ref('real_estate_app.email_template_real_estate_notification_owner_refuse')
        for rec in self:
            template.send_mail(rec.id, force_send=True)

    def action_cancel(self):
        self.state = 'cancel'

    def send_email(self):
        self.state = 'send_email'
        template = self.env.ref('real_estate_app.email_template_real_estate_notification_user')
        for rec in self:
            template.send_mail(rec.id, force_send=True)

"""method to check dates"""
@api.constrains('date_debut', 'date_fin')
def _check_dates(self):
    for record in self:
        if record.date_debut and record.date_fin:
            if record.date_debut > record.date_fin:
                raise ValidationError("The end date must be after the start date.")
