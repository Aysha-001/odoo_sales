from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_reference_id = fields.Char(string="Customer Reference")