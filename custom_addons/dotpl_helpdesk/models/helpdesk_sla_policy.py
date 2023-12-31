from odoo import api, fields, models, _


class HelpdeskSlaPolicy(models.Model):
    _name = "helpdesk.sla.policy"
    _description = "Helpdesk SLA Policies"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
