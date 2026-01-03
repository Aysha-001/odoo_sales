{
    'name': 'new sales',
    'version': '1.0',
    'summary': 'custom sales app',
    'description': 'my custom sales app',
    'author': 'You',
    'license': 'LGPL-3',
    'depends': ['sale',
    'stock',
    'sale_stock',],
    'data': [
        'security/ir.model.access.csv',
        'views/account_view_new.xml',
        'views/stock_picking_view.xml',
        'views/sale_order_view_new.xml',
        'views/wizard_view.xml',
        'views/sale_order_task_view.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
}
