# -*- coding: utf-8 -*-
{
    'name': "Advanced Search Filters",
    'version': '11.4.0.0.0',
    'summary': """
        Adds Today, This Week and This Month Filter in Sale Order, Invoice and Payment""",

    'description': """
        Adds Today, This Week and This Month Filter in Sale Order, Invoice and Payment
    """,

    'author': "10 Orbits",
    'website': "http://www.10orbits.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase'],
    'images': ['static/description/banner.png'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/account_invoice.xml',
        'views/account_payment.xml',
        'views/sale_report.xml',
        'views/css.xml',

        # 'views/templates.xml',
    ],
    'license': 'AGPL-3',
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
