from odoo import api, fields, models, _


class FleetVehicleInheritance(models.Model):
    _inherit = 'fleet.vehicle'

    ownership = fields.Char(string='Ownership')

    branch_id = fields.Many2one('fleet.branch', string='Branch')
    hub_id = fields.Many2one('fleet.hub', string='Hub', domain="[('branch_id', '=', branch_id)]")
    document_ids = fields.One2many('fleet.document', 'vehicle_id', string='Documents', domain=[('state', 'in', ('active', 'expired', 'hold'))])
    history_document_ids = fields.One2many('fleet.document', 'vehicle_id', string='History Documents', domain=[('state', '=', 'renewed')])



