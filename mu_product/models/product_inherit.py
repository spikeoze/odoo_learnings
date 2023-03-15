from odoo import api, fields, models, _, tools


class Product(models.Model):
    _inherit = 'product.template'
    
    
    product_description = fields.Char(string='Product Description')
    