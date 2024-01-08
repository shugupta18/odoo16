from random import randint

from odoo import api, fields, models, _


class DocumentTag(models.Model):
    _name = "fleet.document.tag"
    _description = "Fleet Document Tag"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color', default=10)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A tag with the same name already exists."),
    ]
