from odoo import api, fields, models, _


class FleetHub(models.Model):
    _name = "fleet.hub"
    _description = "Fleet Hub (custom)"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    lat = fields.Char(string='Latitude')
    long = fields.Char(string='Longitude')

    erp_code = fields.Char(string='ERP Code', tracking=True)

    manager = fields.Char(string='Manager', tracking=True)
    fleet_manager = fields.Char(string='Fleet Manager', tracking=True)
    manager_email = fields.Char(string='Manager Email', tracking=True)
    fleet_manager_email = fields.Char(string='Fleet Manager Email', tracking=True)

    email = fields.Char(string='Hub Email')
    operations_email = fields.Char(string='Hub Operations Email')
    fleet_email = fields.Char(string='Hub Fleet Email')

    branch_id = fields.Many2one('fleet.branch', string="Branch")

