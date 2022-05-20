# -*- coding: utf-8 -*-
{
    'name': "Star Line Sale",
    'summary': """ Changes in Sale order and reflect the changes in invoice """,
    'description': """
         Changes in Sale order and reflect the changes in invoice
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', "sale", "stock"],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
