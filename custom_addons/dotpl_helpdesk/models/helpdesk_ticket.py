from odoo import api, fields, models, _

from datetime import timedelta

TICKET_PRIORITY = [('0', 'Very Low'), ('1', 'Low'), ('2', 'Moderate'), ('3', 'High'), ('4', 'Very High')]


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_stage_id(self):
        stage_id = self.env['helpdesk.stage'].search([], order='sequence asc, id asc', limit=1)
        return stage_id

    name = fields.Char(string='Name', required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    stage_id = fields.Many2one(comodel_name='helpdesk.stage', string='Stage', default=_default_stage_id, tracking=1)

    created_datetime = fields.Datetime(string='Created Datetime', default=fields.Datetime.now, tracking=True)
    ticket_number = fields.Char(string='Ticket Number', readonly=True)

    category_id = fields.Many2one(comodel_name='helpdesk.ticket.category', string='Category', tracking=True)
    issue_regarding = fields.Char(string='Issue Regarding', tracking=True)
    source_id = fields.Many2one(comodel_name='helpdesk.ticket.source', string='Source', help='Source of the ticket', tracking=True)

    description = fields.Html(string='Description')

    team_id = fields.Many2one(comodel_name='helpdesk.team', string='Assigned Team', tracking=True)
    possible_team_member_ids = fields.Many2many(related='team_id.member_ids')
    member_id = fields.Many2one(comodel_name='res.users', string='Assigned To', domain="[('id', 'in', possible_team_member_ids)]", tracking=True)
    priority = fields.Selection(selection=TICKET_PRIORITY, string='Priority', default='1', tracking=True)
    tag_ids = fields.Many2many(comodel_name='helpdesk.tag', string='Tags')
    sla_deadline = fields.Datetime(string='SLA Deadline')
    closing_datetime = fields.Datetime(string='Closing Datetime')

    customer_name = fields.Char(string='Customer Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email Id')
    cc_email = fields.Char(string='cc Email')
    uploaded_document = fields.Binary(string='Document', attachment=True)

    @api.onchange('created_datetime', 'priority')
    def onchange_created_datetime_priority(self):
        sla_policies = self.env['helpdesk.sla.policy'].search([('priority', '=', self.priority)],
                                                              order='id desc', limit=1)
        if sla_policies:
            duration = timedelta(hours=sla_policies[0].time)
            self.sla_deadline = self.created_datetime + duration

    @api.onchange('stage_id')
    def onchange_stage_id(self):
        if self.stage_id.name == 'Closed':
            self.closing_datetime = fields.datetime.now()

    # ------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------


    @api.model
    def create(self, vals):
        vals['ticket_number'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket')
        return super(HelpdeskTicket, self).create(vals)

