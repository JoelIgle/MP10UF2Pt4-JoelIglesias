{
"name": "Sales",
"version": "16.0.0",
"application": True,
"depends": ["base", "sale"],
"data": [
     'security/ir.model.access.csv',
     'views/sales_views.xml',
     'reports/report_saleorder.xml',
     'views/sale_order_menu.xml',
     'views/sales_report_view.xml',
     'reports/saleorder_report_personalitzat.xml',
     'reports/saleorder_templates.xml'
],
"installable": True,
'license': 'LGPL-3',
}