from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HelpdeskStage(models.Model):
    _name = 'helpdesk.stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    sequence = fields.Integer(string='Sequence', default=10)

    team_ids = fields.Many2many(comodel_name='helpdesk.team', relation='stage_team_rel', string='Helpdesk Teams',
                                required=True)
    description = fields.Text(string='Description', translate=True)
    fold = fields.Boolean(string='Folded in Kanban', default=True)

    # ------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------

    def unlink(self):
        if self.name in ['Open', 'In Progress', 'Closed']:
            raise ValidationError(_("Stages: {'Open', 'In Progress', 'Closed'} cannot be deleted!"))
        return super(HelpdeskStage, self).unlink()

    def write(self, vals):
        if 'active' in vals and not vals['active'] and self.name in ['Open', 'In Progress', 'Closed']:
            raise ValidationError(_("Stages: {'Open', 'In Progress', 'Closed'} cannot be archived!"))
        return super(HelpdeskStage, self).write(vals)
