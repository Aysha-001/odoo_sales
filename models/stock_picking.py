from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    #customer_reference_id = fields.Char(
    #    string="Customer Reference",
    #    related="sale_id.customer_reference_id",
    #    store=True,
    #    readonly=True
    #)

    customer_reference_id = fields.Char("Customer Reference")

    sale_tag_ids = fields.Many2many('sale.order.tag', string='Tags')

    @api.model
    def create(self, vals):
        picking = super().create(vals)

        if picking.sale_id:
            picking.customer_reference_id = picking.sale_id.customer_reference_id

        return picking