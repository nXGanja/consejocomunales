# -*- coding: utf-8 -*-
{
    'name': "Familias",

    'summary': """
        Modulo para el Control de las Familias Pertenecientes a un Consejo Comunal""",

    'description': """
        Long description of module's purpose
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
        'vistas/familias_view.xml',
        'vistas/apartamentos_view.xml',
        'vistas/pisos_view.xml',
    ],
    # only loaded in demonstration mode

}