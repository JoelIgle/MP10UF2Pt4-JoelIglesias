from odoo import models, fields, api


class Sales(models.Model):
    _inherit = 'sale.order'

    item_count = fields.Integer('Nombre d’articles', compute='_compute_item_count')
    preferred_email = fields.Char('Adreça de correu preferencial')


    @api.depends('order_line')
    def _compute_item_count(self):
        # Itera sobre totes les ordres
        for order in self:
            order.item_count = len(order.order_line)
