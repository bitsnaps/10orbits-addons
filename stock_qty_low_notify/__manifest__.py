{
    'name' : 'Low Stock Quantity Notification',
    'version' : '1.0',
    'author' : '10 Orbits',
    'summary' : ' This modules is used for sending notification once stock of a product goes below specified amount.',
    'description' : 'The main purpose of this module is to send notification to the inventory manager about low stock avaliability.',
    'category' : 'Sales Management',
    'depends' : ['base', 'mail', 'product'],
    'images': ['static/description/banner.png'],
    'data':[
                'views/product_template.xml',
                'views/ir_cron.xml'
    		],
    'installable': True,
    'license': 'AGPL-3',

}
