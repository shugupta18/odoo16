# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dotpl_fleet(models.Model):
#     _name = 'dotpl_fleet.dotpl_fleet'
#     _description = 'dotpl_fleet.dotpl_fleet'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

