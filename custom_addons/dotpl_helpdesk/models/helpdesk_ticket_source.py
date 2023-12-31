from odoo import api, fields, models, _


class HelpdeskTicketCategory(models.Model):
    _name = "helpdesk.ticket.source"
    _description = "Helpdesk Ticket Source"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
