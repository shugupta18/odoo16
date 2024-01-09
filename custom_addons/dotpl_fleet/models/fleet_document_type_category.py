from odoo import api, fields, models, _


class DocumentTypeCategory(models.Model):
    _name = "fleet.document.type.category"
    _description = "Document Type Category"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "A category with the same name already exists."),
    ]
