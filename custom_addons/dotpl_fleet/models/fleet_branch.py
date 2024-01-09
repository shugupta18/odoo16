from odoo import api, fields, models, _


class FleetBranch(models.Model):
    _name = "fleet.branch"
    _description = "Fleet Branch (custom)"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    lat = fields.Char(string='Branch Latitude')
    long = fields.Char(string='Branch Longitude')

    erp_code = fields.Char(string='Hub ERP Code', tracking=True)

    manager = fields.Char(string='Manager Name', tracking=True)
    fleet_manager = fields.Char(string='Fleet Manager Name', tracking=True)
    manager_email = fields.Char(string='Manager Email', tracking=True)
    fleet_manager_email = fields.Char(string='Fleet Manager Email', tracking=True)

    hub_ids = fields.One2many(comodel_name='fleet.hub', inverse_name='branch_id', string='Hubs')
    hub_count = fields.Integer(string='', compute='_compute_hub_count', store=True)

    @api.depends('hub_ids')
    def _compute_hub_count(self):
        for branch in self:
            branch.hub_count = len(branch.hub_ids)

    def action_view_hubs(self):
        action = self.env.ref('dotpl_fleet.action_fleet_hub').read()[0]
        action['domain'] = [('branch_id', '=', self.id)]
        action['context'] = {'default_branch_id': self.id}
        return action
