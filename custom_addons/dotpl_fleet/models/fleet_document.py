from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _


class FleetDocument(models.Model):
    _name = "fleet.document"
    _description = 'Fleet Document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    def name_get(self):
        return [(record.id, f"{record.document_type_id.name}: {record.issue_date}") for record in self]

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
    recurring_flag = fields.Boolean(string='Is Recurring?', related='document_type_id.recurring_flag', store=False)


    @api.onchange('issue_date', 'vehicle_id')
    def _onchange_issue_date_vehicle(self):
        if self.issue_date and self.document_type_id and self.document_type_id.expire_in_days:
            self.expiry_date = self.issue_date + relativedelta(days=self.document_type_id.expire_in_days)
        else:
            self.expiry_date = False

    @api.onchange('document_type_id')
    def _onchange_document_type(self):
        if self.document_type_id and not self.document_type_id.recurring_flag:
            self.new_flag = True


    @api.model
    def create_renewed_document(self):
        new_document = self.create({
            'issue_date': fields.Date.today(),
            'expiry_date': fields.Date.today() + relativedelta(days=self.document_type_id.expire_in_days),
            'state': 'active',
            'vehicle_id': self.vehicle_id.id,
            'document_type_id': self.document_type_id.id,
        })
        self.write({'state': 'renewed', 'new_flag': False})
        return new_document

    def action_renew_document(self):
        new_document = self.create_renewed_document()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'fleet.document',
            'res_id': new_document.id,
            'view_mode': 'form',
            'view_id': False,
            'target': 'current',
        }
