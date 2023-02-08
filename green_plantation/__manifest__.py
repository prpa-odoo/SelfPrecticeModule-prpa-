{
    'name': 'Green Plantation',
    'application':True,
    'sequence':-100,
    'version': '1.0',
    'depends': ['base'],
    'author': 'Priyanshi',
    'category': 'Category',
    'summary': 'Self Module Training',
    'license': 'LGPL-3',
    'installable': True,
    'data' : [
        'security/ir.model.access.csv',
        'views/user_view.xml',
        'views/product_view.xml',
        'views/order_view.xml',
        'views/plant_menus.xml'     
    ]
}