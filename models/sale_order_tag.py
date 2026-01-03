from odoo import models, fields

class SaleOrderTag(models.Model):
    _name = 'sale.order.tag'
    _description = 'Sales Order Tags'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index') # Allows the colorful bubbles