from odoo import api, fields, models, _


class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "Helpdesk Team"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
