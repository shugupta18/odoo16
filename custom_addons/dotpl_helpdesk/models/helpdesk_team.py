import datetime

from dateutil import relativedelta

from odoo import api, fields, models, _


class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _description = "Helpdesk Team"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', index=True,
                                  default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency",
                                  related='company_id.currency_id', readonly=True)
    user_id = fields.Many2one('res.users', string='Team Leader', check_company=True)

    email_alias = fields.Char(string='Email Alias')
    team_leader = fields.Char(string='Team Leader')
    color = fields.Integer(string='Color Index', help="The color of the channel")

    member_ids = fields.Many2many(comodel_name='res.users', string='Members',
                                  help="Users assigned to this team.")

    ticket_closed = fields.Integer(string='Ticket Closed', compute='_compute_ticket_closed')
    open_ticket_count = fields.Integer(string='Open Ticket Count', compute='_compute_open_ticket_count')
    unassigned_tickets = fields.Integer(string='Unassigned Ticket Count', compute='_compute_unassigned_tickets')
    urgent_ticket = fields.Integer(string='Urgent Ticket Count', compute='_compute_urgent_ticket')
    sla_failed = fields.Integer(string='Sla Failed Count', compute='_compute_sla_failed')

    def _compute_ticket_closed(self):
        # multiple self records
        dt = datetime.datetime.combine(datetime.date.today() - relativedelta.relativedelta(days=6), datetime.time.min)
        for team in self:
            team.ticket_closed = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id),
                ('state', '=', 'close'),
                ('closing_datetime', '>=', dt)
            ])

    def _compute_open_ticket_count(self):
        # multiple self records
        for team in self:
            team.open_ticket_count = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id),
                ('state', '=', 'open')
            ])

    def _compute_unassigned_tickets(self):
        # multiple self records
        # if stage in [new, open, in_progress] AND team is assigned but no team member is assigned
        for team in self:
            team.unassigned_tickets = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id),
                ('state', 'in', ['new', 'open', 'in_progress'])
            ])

    def _compute_urgent_ticket(self):
        # multiple self records
        for team in self:
            team.urgent_ticket = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id),
                ('state', 'in', ['new', 'open', 'in_progress']),
                ('priority', '>=', 3)
            ])

    def _compute_sla_failed(self):
        # multiple self records
        for team in self:
            team.sla_failed = self.env['helpdesk.ticket'].search_count([
                ('team_id', '=', team.id),
                ('state', 'in', ['new', 'open', 'in_progress']),
                ('sla_deadline', '<', fields.Datetime.now())
            ])
    # ------------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------------

    def action_primary_channel_button(self):
        print('action_primary_channel_button button pressed')
        return
    def action_view_ticket(self):
        print('action_view_ticket button pressed')
        return

    def action_view_closed_ticket(self):
        print('action_view_closed_ticket button pressed')
        return


    def action_view_open_ticket(self):
        print('action_view_open_ticket action pressed!')
        return

    def action_test(self):
        print('action_test action pressed!')
        return

    def action_view_urgent(self):
        print('action_view_urgent action pressed!')
        return

    def action_view_sla_failed(self):
        print('action_view_sla_failed action pressed!')
        return

