# -*- coding: utf-8 -*-
{
    'name': "CinemaModule",

    'summary': """Cinema club""",

    'description': """Module to manage movies:""",


    'author': "Sandra Pérez",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Rubricas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/movie.xml',
        'views/actor.xml',
        'views/director.xml',
        'views/studio.xml',
        'views/producer.xml'


    ],
}
