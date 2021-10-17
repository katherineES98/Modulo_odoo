# -*- coding: utf-8 -*-
{
    'name': "Open_Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       Módulo Open Academy para la gestión de formaciones:
            - cursos de formación
            - sesiones de entrenamiento
            - registro de asistentes
    """,

    'author': "My company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cursos Web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course.xml', 
        'views/partner.xml',  
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
