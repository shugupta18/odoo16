from odoo import api, fields, models, _


class HelpdeskTeamMember(models.Model):
    _name = "helpdesk.team.member"
    _description = "Helpdesk Team Member"

    active = fields.Boolean(string='Active', default=True)

    name = fields.Char(string='name')
    user_id = fields.Many2one(comodel_name='res.users', required=True)
    team_id = fields.Many2one(comodel_name='helpdesk.team', string='Helpdesk Team')
    # name = fields.Char(string='Name', related='user_id.display_name', readonly=False)
    # email = fields.Char(string='Email', related='user_id.email')
    # phone = fields.Char(string='Phone', related='user_id.phone')
    # mobile = fields.Char(string='Mobile', related='user_id.mobile')
