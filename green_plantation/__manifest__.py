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
        'views/plant_product_view.xml',
        'views/product_category_plant.xml',
        'views/product_category_fertilizer.xml',
        'views/product_category_seeds.xml',
        'views/product_category_soil.xml',
        'views/product_category_water.xml',
        'views/product_category_plant_product.xml',
        'views/product_vendor.xml',
        'views/plant_weather.xml',
        'views/order_view.xml',
        'views/plant_medicine.xml',
        'views/plant_menus.xml'     
    ]
}