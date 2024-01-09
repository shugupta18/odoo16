from odoo import api, fields, models, _


class FleetVehicleInheritance(models.Model):
    _inherit = 'fleet.vehicle'

    document_line_ids = fields.One2many('fleet.vehicle.document.lines', inverse_name='vehicle_id',
                                        string='Document lines')
    branch_id = fields.Many2one('fleet.branch', string='Branch')
    hub_id = fields.Many2one('fleet.hub', string='Hub', domain="[('branch_id', '=', branch_id)]")



class FleetVehicleDocumentLines(models.Model):
    _name = "fleet.vehicle.document.lines"
    _description = 'fleet vehicle document lines'

    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle')

    document_type_id = fields.Many2one('fleet.document.type', required=True)
    issue_date = fields.Date(string='Issue Date', required=True)
    expiry_date = fields.Date(string='Expiry Date')
    file_data = fields.Binary(string='Attachment')
    file_name = fields.Char(string='File Name')

    remarks = fields.Text(string='Remarks')
    tag_ids = fields.Many2many('fleet.document.tag', string='Tags')
    new_old_toggle = fields.Boolean(string='New/Old')
    state = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('renewed', 'Renewed'),
        ('hold', 'Hold'),
    ], string='State', default='active')
