from odoo import api, fields, models, _


class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "Helpdesk Team"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', index=True,
                                  default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency",
                                  related='company_id.currency_id', readonly=True)
    user_id = fields.Many2one('res.users', string='Team Leader', check_company=True)

    email_alias = fields.Char(string='Email Alias')
    team_leader = fields.Char(string='Team Leader')
    color = fields.Integer(string='Color Index', help="The color of the channel")

    member_ids = fields.Many2many(comodel_name='res.users', string='Members',
                                  help="Users assigned to this team.")


    def action_primary_channel_button(self):
        print('Tickets button pressed')
        return
