# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritSaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    weight = fields.Float("Weight(gram)")
    total_weight = fields.Float("Total Weight (kg)")
    rate_per_kg = fields.Float("Rate/Kg")

    def _prepare_invoice_line(self, **optional_values):
        res = super(InheritSaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res.update({'weight': self.weight,
                    'total_weight': self.total_weight,
                    'rate_per_kg': self.rate_per_kg})
        return res


class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("order_line", "order_line")
    def _onchange_product_id_star_line(self):
        for rec in self:
            for line in rec.order_line:
                line.weight = line.product_id.weight * 1000
                line.total_weight = (line.product_id.weight * line.product_uom_qty)
                line.rate_per_kg = line.price_subtotal / line.total_weight

    def action_confirm(self):
        res = super(InheritSaleOrder, self).action_confirm()
        for rec in self:
            for line in rec.order_line:
                line.move_ids.move_line_ids.weight = line.total_weight
                line.move_ids.weight = line.total_weight
        return res


class InheritStockMove(models.Model):
    _inherit = "stock.move"

    weight = fields.Float("Total Weight (kg)")


class InheritStockMoveLine(models.Model):
    _inherit = "stock.move.line"

    weight = fields.Float("Total Weight (kg)")


class InheritAccountMoveLine(models.Model):
    _inherit = "account.move.line"

    weight = fields.Float("Weight")
    total_weight = fields.Float("Total Weight")
    rate_per_kg = fields.Float("Rate/Kg")
