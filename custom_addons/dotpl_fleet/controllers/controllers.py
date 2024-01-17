# -*- coding: utf-8 -*-
# from odoo import http


# class DotplFleet(http.Controller):
#     @http.route('/dotpl_fleet/dotpl_fleet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dotpl_fleet/dotpl_fleet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dotpl_fleet.listing', {
#             'root': '/dotpl_fleet/dotpl_fleet',
#             'objects': http.request.env['dotpl_fleet.dotpl_fleet'].search([]),
#         })

#     @http.route('/dotpl_fleet/dotpl_fleet/objects/<model("dotpl_fleet.dotpl_fleet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dotpl_fleet.object', {
#             'object': obj
#         })
