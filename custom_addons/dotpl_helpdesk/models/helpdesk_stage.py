from odoo import api, fields, models, _


class HelpdeskStage(models.Model):
    _name = 'helpdesk.stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence, id'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', translate=True)
    sequence = fields.Integer(string='Sequence', default=10)

    team_ids = fields.Many2many(comodel_name='helpdesk.team', relation='stage_team_rel', string='Helpdesk Teams',
                                required=True)
