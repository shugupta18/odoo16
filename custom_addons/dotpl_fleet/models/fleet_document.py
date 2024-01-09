from odoo import api, fields, models, _


class FleetDocumemnt(models.Model):
    _name = "fleet.document"
    _description = 'Fleet Document'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string="Active", default=True)
