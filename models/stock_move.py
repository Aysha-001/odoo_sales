from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        res = super()._get_new_picking_values()
        # 'self.sale_line_id.order_id' reaches back to the Sale Order
        move = self[:1]
        if move.sale_line_id.order_id:
            res['sale_tag_ids'] = [(6, 0, move.sale_line_id.order_id.tag_ids.ids)]
        return res