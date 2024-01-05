from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class WizardHelpdeskCancelTicket(models.TransientModel):
    _name = "helpdesk.cancel.ticket.wizard"
    _description = "Cancel Ticket Wizard"

    reason = fields.Text(string='Reason', required=True)
    cancel_date = fields.Date(string='Cancellation Date')


    def action_cancel_button(self):
        for record in self:
            ticket_id = self.env.context.get('active_id')
            ticket = record.env['helpdesk.ticket'].browse(ticket_id)
            ticket.write({
                'state': 'cancel',
            })
        return {'type': 'ir.actions.act_window_close'}


class WizardHelpdeskCloseTicket(models.TransientModel):
    _name = "helpdesk.close.ticket.wizard"
    _description = "Close Ticket Wizard"

    closing_remarks_category = fields.Selection([('not_an_issue', 'Not an Issue'), ('resolved', 'Resolved')],
                                                string='Closing Remarks Category')
    closing_remarks = fields.Text(string='Closing Remarks')

    def action_close_button(self):
        for record in self:
            ticket_id = self.env.context.get('active_id')
            ticket = record.env['helpdesk.ticket'].browse(ticket_id)
            ticket.write({
                'closing_remarks_category': self.closing_remarks_category,
                'closing_remarks': self.closing_remarks,
                'state': 'close',
                'closing_datetime': fields.Datetime.now(),
            })
        return {'type': 'ir.actions.act_window_close'}

