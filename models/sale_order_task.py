from odoo import models, fields

class SaleOrderTask(models.Model):
    _name = 'sale.order.task'
    _description = 'Simple Follow-up Task'

    order_id = fields.Many2one('sale.order', ondelete='cascade')
    name = fields.Char(string="Task Description", required=True)
    status = fields.Selection([
        ('todo', 'To Do'),
        ('done', 'Completed')
    ], string="Status", default='todo')