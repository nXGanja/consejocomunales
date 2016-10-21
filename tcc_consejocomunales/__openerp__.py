# -*- coding: utf-8 -*-
{
    'name': "Gestion Comunal",

    'summary': """
        Sistema Para la Gestion de Consejos Comunales""",

    'description': """
        Sistema Realizado Para la Gestion de Consejos Comunales en General
    """,

    'author': "Javier Montesinos",
    'website': "http://www.tuconsejocomunal.com.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gestion Comunal',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'vistas/consejo_comunal_view.xml',
        'vistas/estados_view.xml',
        'vistas/municipios_view.xml',
        'vistas/parroquias_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}