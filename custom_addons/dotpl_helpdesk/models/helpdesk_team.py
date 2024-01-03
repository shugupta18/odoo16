from odoo import api, fields, models, _


class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "Helpdesk Team"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)

    email_alias = fields.Char(string='Email Alias')
    team_leader = fields.Char(string='Team Leader')

    member_ids = fields.Many2many(comodel_name='res.users', string='Members', help="Users assigned to this team.")
