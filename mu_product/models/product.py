from odoo import api, fields, models, _, tools


class ProductSale(models.Model):
    _name = "product.sale"
    _description = "Product Sale"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    reference = fields.Char(
        string="Reference",
        readonly=True,
        required=True,
        copy=False,
        default=lambda self: _("New"),
    )

    name = fields.Char(
        string="Name",
        required=True,
        tracking=True,
    )
    price = fields.Integer(
        String="Price",
        required=True,
        tracking=True,
    )
    description = fields.Text(
        String="Description",
        tracking=True,
    )
    category = fields.Selection(
        string="Category",
        tracking=True,
        selection=[("watch", "Watch"), ("tv", "Tv"), ("other", "Other")],
    )

    producer_id = fields.Many2one(
        string="Producer",
        comodel_name="hospital.patient",
    )

    @api.model
    def create(self, values):
        if not values.get("description"):
            values["description"] = "New Product"

        if values.get("reference", _("New")) == _("New"):
            values["reference"] = self.env["ir.sequence"].next_by_code("product.sale") or _("New")

        result = super(ProductSale, self).create(values)

        return result
