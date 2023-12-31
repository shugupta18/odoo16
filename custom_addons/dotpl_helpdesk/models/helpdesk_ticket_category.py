from odoo import api, fields, models, _


class HelpdeskTicketCategory(models.Model):
    _name = "helpdesk.ticket.category"
    _description = "Helpdesk Ticket Category"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
