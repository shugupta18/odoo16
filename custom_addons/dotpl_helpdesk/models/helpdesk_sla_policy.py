
from odoo import api, fields, models, _

TICKET_PRIORITY = [('0', 'Very Low'), ('1', 'Low'), ('2', 'Moderate'), ('3', 'High'), ('4', 'Very High')]


class HelpdeskSlaPolicy(models.Model):
    _name = "helpdesk.sla.policy"
    _description = "Helpdesk SLA Policies"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    priority = fields.Selection(TICKET_PRIORITY, string='Priority')
