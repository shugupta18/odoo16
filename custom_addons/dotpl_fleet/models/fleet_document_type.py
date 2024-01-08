from odoo import api, fields, models, _


class DocumentType(models.Model):
    _name = "fleet.document.type"
    _description = "Document Type"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True, tracking=True)

    expire_in_days = fields.Integer(string='Expire in (Days)', tracking=True)
    reminder_required_in_days = fields.Integer(string='Reminder Required in (Days)', tracking=True)
