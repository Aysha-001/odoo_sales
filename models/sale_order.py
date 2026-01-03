from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference_id = fields.Char("Customer Reference")

    regional_manager_id = fields.Many2one('res.users', string="Regional Manager")

    tag_ids = fields.Many2many('sale.order.tag', string='Tags')

    task_ids = fields.One2many('sale.order.task', 'order_id', string="Task")

    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        values.update({
            'customer_reference_id': self.customer_reference_id,  # Pass sale field to invoice
        })
        return values


