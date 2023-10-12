# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    userrr_amount_fees = fields.Monetary(currency_field="currency_id", string="Order Fees/Discounts")
    userrr_amount_tax = fields.Monetary(currency_field="currency_id", string="Order Taxes")
    userrr_amount_shipping = fields.Monetary(currency_field="currency_id", string="Total Shipping")
    userrr_amount_total = fields.Monetary(currency_field="currency_id", string="Order Total")