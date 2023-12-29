# -*- coding: utf-8 -*-
# from odoo import http


# class DotplHelpdesk(http.Controller):
#     @http.route('/dotpl_helpdesk/dotpl_helpdesk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dotpl_helpdesk/dotpl_helpdesk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dotpl_helpdesk.listing', {
#             'root': '/dotpl_helpdesk/dotpl_helpdesk',
#             'objects': http.request.env['dotpl_helpdesk.dotpl_helpdesk'].search([]),
#         })

#     @http.route('/dotpl_helpdesk/dotpl_helpdesk/objects/<model("dotpl_helpdesk.dotpl_helpdesk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dotpl_helpdesk.object', {
#             'object': obj
#         })

