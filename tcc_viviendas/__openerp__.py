# -*- coding: utf-8 -*-
{
    'name': "Viviendas",

    'summary': """
        Este Modulo es para el control de las viviendas de los consejos comunales""",

    'description': """
       Este Modulo es para la Gestion y control de las viviendas de los consejos comunales
    """,

    'author': "Javier Montesinos",
    'website': "http://www.tuconsejocomunal.com.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'vistas/viviendas_view.xml',
        'vistas/casas_view.xml',
        'vistas/edificios_view.xml',
        'vistas/callesoavenidas_view.xml',
        'vistas/sectores_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}