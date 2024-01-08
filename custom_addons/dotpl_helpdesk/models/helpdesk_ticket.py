from odoo import api, fields, models, _

from datetime import timedelta

TICKET_PRIORITY = [('0', 'Very Low'), ('1', 'Low'), ('2', 'Moderate'), ('3', 'High'), ('4', 'Very High')]
TICKET_STATES = [('new', 'New'), ('open', 'Open'), ('in_progress', 'In Progress'),
                ('close', 'Close'), ('cancel', 'Cancel')]
CLOSING_REMARKS_CATEGORY = [('not_an_issue', 'Not an Issue'), ('resolved', 'Resolved')]


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _description = "Helpdesk Ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _default_stage_id(self):
        stage_id = self.env['helpdesk.stage'].search([], order='sequence asc, id asc', limit=1)
        return stage_id

    name = fields.Char(string='Name', required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    state = fields.Selection(TICKET_STATES, string="Status", default='new', required=True, tracking=True)
    stage_id = fields.Many2one(comodel_name='helpdesk.stage', string='Stage', default=_default_stage_id, tracking=1)

    ticket_number = fields.Char(string='Ticket Number', readonly=True)
    created_datetime = fields.Datetime(string='Created Datetime', default=fields.Datetime.now, tracking=True)
    opened_datetime = fields.Datetime(string='Opened Datetime', tracking=True)

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
    opening_datetime = fields.Datetime(string='Opening Datetime')
    closing_datetime = fields.Datetime(string='Closing Datetime')
    closing_remarks_category = fields.Selection(CLOSING_REMARKS_CATEGORY, string='Closing Remarks Category', tracking=True)
    closing_remarks = fields.Text(string='Closing Remarks', tracking=True)
    reopening_datetime = fields.Datetime(string='Reopening Datetime')

    customer_id = fields.Many2one(
        'res.partner', string='Customer', index=True, tracking=10)
    customer_name = fields.Char(string='Customer Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email Id')
    cc_email = fields.Char(string='cc Email')
    uploaded_document = fields.Binary(string='Document', attachment=True)

    # sla related fields below
    # sla_fail = fields.Boolean("Failed SLA Policy")

    @api.onchange('created_datetime', 'priority')
    def onchange_created_datetime_priority(self):
        sla_policies = self.env['helpdesk.sla.policy'].search([('priority', '=', self.priority)],
                                                              order='id desc', limit=1)
        if sla_policies:
            duration = timedelta(hours=sla_policies[0].time)
            self.sla_deadline = self.created_datetime + duration

    # ------------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------------

    def action_open(self):
        for record in self:
            if record.state == 'new':
                record.opening_datetime = fields.Datetime.now()
                record.state = 'open'

    def action_in_progress(self):
        for record in self:
            if record.state == 'open':
                record.state = 'in_progress'

    def action_close(self):
        for record in self:
            if record.state == 'in_progress':
                record.state = 'close'

    def action_cancel(self):
        for record in self:
            if record.state in ('new', 'open', 'in_progress'):
                record.state = 'cancel'

    def action_reopen(self):
        for record in self:
            if record.state in ('close', 'cancel'):
                record.reopening_datetime = fields.Datetime.now()
                record.state = 'open'

    # ------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------


    @api.model
    def create(self, vals):
        vals['ticket_number'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket')
        return super(HelpdeskTicket, self).create(vals)

    # ------------------------------------------------------------
    # Wizard
    # ------------------------------------------------------------

    def open_close_ticket_wizard(self):
        action = self.env.ref('dotpl_helpdesk.action_helpdesk_close_ticket').read()[0]
        return action

    def open_cancel_ticket_wizard(self):
        action = self.env.ref('dotpl_helpdesk.action_helpdesk_cancel_ticket').read()[0]
        return action
