from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string="Sale Description")
