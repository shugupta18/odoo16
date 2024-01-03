
from odoo import api, fields, models, _

TICKET_PRIORITY = [('0', 'Very Low'), ('1', 'Low'), ('2', 'Moderate'), ('3', 'High'), ('4', 'Very High')]


class HelpdeskSlaPolicy(models.Model):
    _name = "helpdesk.sla.policy"
    _description = "Helpdesk SLA Policies"
    _order = 'id desc'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    priority = fields.Selection(TICKET_PRIORITY, string='Priority', required=True)
    time = fields.Float(string='Within', default=0, required=True,
                        help='Maximum number of working hours a ticket should take to reach the target stage, starting from the date it was created.')
