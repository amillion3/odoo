# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    user_amount_tax = fields.Monetary(currency_field="currency_id", string="Order Taxes")
    user_amount_shipping = fields.Monetary(currency_field="currency_id", string="Total Shipping")
