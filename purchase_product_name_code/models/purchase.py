# SPDX-FileCopyrightText: 2026 Coop IT Easy SC
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, fields, models
from odoo.tools import get_lang


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_name = fields.Char(
        compute="_compute_product_name",
        readonly=True,
        store=True,
    )
    product_code = fields.Char(
        string="Product Code",
        related="product_id.code",
        readonly=True,
        store=True,
    )

    @api.depends(
        "product_id",
        "partner_id",
        "product_qty",
        "product_uom",
        "order_id.date_order",
    )
    def _compute_product_name(self):
        for line in self:
            params = line._get_select_sellers_params()
            seller = line.product_id._select_seller(
                partner_id=line.partner_id,
                quantity=line.product_qty,
                date=line.order_id.date_order
                and line.order_id.date_order.date()
                or fields.Date.context_today(line),
                uom_id=line.product_uom,
                params=params,
            )
            product_ctx = {
                "seller_id": seller.id,
                "lang": get_lang(line.env, line.partner_id.lang).code,
            }
            line.product_name = line.product_id.with_context(**product_ctx).name
