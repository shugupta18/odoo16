from odoo import api, fields, models, _


class FleetVehicleModelBrandInheritance(models.Model):
    _inherit = 'fleet.vehicle.model.brand'

    erp_code = fields.Char(string='Manufacturer ERP Code', help='Manufacturer ERP Code')


class FleetVehicleModelInheritance(models.Model):
    _inherit = 'fleet.vehicle.model'

    erp_code = fields.Char(string='Model ERP Code', help='Model ERP Code')
