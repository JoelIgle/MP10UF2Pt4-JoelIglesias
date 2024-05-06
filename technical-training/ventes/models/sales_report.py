from odoo import models, fields, tools, api


class SalesReport(models.Model):
    _name = 'ventes.sales.report'
    _description = 'Sales Report'
    _auto = False

    user_id = fields.Many2one('res.users', 'Salesperson', readonly=True)
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True)
    order_count = fields.Integer('Order Count', readonly=True)
    total_amount = fields.Float('Total Amount', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'ventes_sales_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW ventes_sales_report AS (
                SELECT
                    min(so.id) as id,
                    so.user_id as user_id,
                    so.state as state,
                    count(*) as order_count,
                    sum(so.amount_total) as total_amount,
                    so.company_id as company_id
                FROM
                    sale_order so
                GROUP BY
                    so.user_id,
                    so.state,
                    so.company_id
            )
        """)

    @api.model
    def get_all_data(self):
        # Retorna totes les dades del model
        return self.search([])
