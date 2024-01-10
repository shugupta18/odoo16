from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _


class FleetDocument(models.Model):
    _name = "fleet.document"
    _description = 'Fleet Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name')
    active = fields.Boolean(string="Active", default=True, tracking=True)
    issue_date = fields.Date(string='Issue Date', required=True, tracking=True)
    attachment_data = fields.Binary(string='Attachment')
    attachment_name = fields.Char(string='Attachment Name')
    remarks = fields.Text(string='Remarks')
    tag_ids = fields.Many2many('fleet.document.tag', string='Tags')
    new_flag = fields.Boolean(string='New/Old', default=True, tracking=True, help='True means the document is "New"')
    state = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('renewed', 'Renewed'),
        ('hold', 'Hold'),
    ], string='State', default='active', tracking=True)

    expiry_date = fields.Date(string='Expiry Date', store=True, tracking=True)

    vehicle_id = fields.Many2one(comodel_name='fleet.vehicle', string='Vehicle', required=True, tracking=True)
    document_type_id = fields.Many2one('fleet.document.type', string='Document Type', required=True, tracking=True)

    @api.onchange('issue_date', 'vehicle_id')
    def _onchange_issue_date_vehicle(self):
        if self.issue_date and self.document_type_id and self.document_type_id.expire_in_days:
            self.expiry_date = self.issue_date + relativedelta(days=self.document_type_id.expire_in_days)
        else:
            self.expiry_date = False


# class IrAttachment(models.Model):
#     _inherit = 'ir.attachment'
#     _rec_name = "name"

