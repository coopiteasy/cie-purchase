# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_view_update_standard_price_wizard(self):
        self.mapped("order_line").update_supplierinfo_price()
        self.mapped("order_line").update_product_standard_price()
