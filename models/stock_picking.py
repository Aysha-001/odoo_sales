from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_reference_id = fields.Char(
        string="Customer Reference",
        related="sale_id.customer_reference_id",
        store=True,
        readonly=True
    )

    sale_tag_ids = fields.Many2many('sale.order.tag', string='Tags')