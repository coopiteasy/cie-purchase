# SPDX-FileCopyrightText: 2023 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def update_product_standard_price(self):
        for line in self:
            new_seller_price = line.price_unit
            line.product_id.standard_price = new_seller_price
