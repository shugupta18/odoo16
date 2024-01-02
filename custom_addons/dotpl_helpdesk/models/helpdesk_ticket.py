from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_stage_id(self):
        stage_id = self.env['helpdesk.stage'].search([], order='sequence asc, id asc', limit=1)
        return stage_id

    name = fields.Char(string='Name')
    active = fields.Boolean(string="Active", default=True, tracking=True)
    activity = fields.Char(string='Activity',default='Remove activity')
    stage_id = fields.Many2one(comodel_name='helpdesk.stage', string='Stage', default=_default_stage_id, tracking=1)

    title = fields.Char(string='Title', required=True, tracking=True)
    created_date = fields.Date(string='Created Date', default=fields.Date.context_today)
    ticket_number = fields.Char(string='Ticket Number', readonly=True)

    category_id = fields.Many2one(comodel_name='helpdesk.ticket.category', string='Category', tracking=True)
    issue_regarding = fields.Char(string='Issue Regarding', tracking=True)
    source_id = fields.Many2one(comodel_name='helpdesk.ticket.source', string='Source', help='Source of the ticket', tracking=True)

    description = fields.Html(string='Description')

    team_id = fields.Many2one(comodel_name='helpdesk.team', string='Assigned Team', tracking=True)
    possible_team_member_ids = fields.Many2many(related='team_id.member_ids')
    member_id = fields.Many2one(comodel_name='res.users', string='Assigned To', tracking=True, domain="[('id', 'in', possible_team_member_ids)]")
    priority = fields.Selection(selection=[('0', 'Normal'), ('1', 'Low'), ('2', 'Moderate'), ('3', 'High'), ('4', 'Very High')], string='Priority', tracking=True)
    tag_ids = fields.Many2many(comodel_name='helpdesk.tag', string='Tags')
    estimated_closing_date = fields.Date(string='Estimated Closing Date')
    closing_date = fields.Date(string='Closing Date')

    customer_name = fields.Char(string='Customer Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email Id')
    cc_email = fields.Char(string='cc Email')
    uploaded_document = fields.Binary(string='Document', attachment=True)

    # @api.depends('team_id')
    # def _compute_member_id(self):
    #     for record in self:
    #         members = record.team_id.member_ids
    #         record.team_member_id = members and members[0] or False

    # ------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------

    @api.model
    def create(self, vals):
        vals['ticket_number'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket')
        return super(HelpdeskTicket, self).create(vals)

