# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    user_amount_fees = fields.Monetary(currency_field="currency_id", string="Order Fees/Discounts")
    user_amount_tax = fields.Monetary(currency_field="currency_id", string="Order Taxes")
    user_amount_shipping = fields.Monetary(currency_field="currency_id", string="Total Shipping")
    user_amount_total = fields.Monetary(currency_field="currency_id", string="Order Total")