{
    'name': "Fleet - MOD",
    'summary': """Fleet module customization by dotpl""",
    'description': """Fleet module customization by dotpl""",
    'author': "DOTPL",
    'website': "https://digitalorder.in",
    'category': 'Fleet',
    'version': '1.0',
    'sequence': -200,

    'depends': ['fleet', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_branch_views.xml',
        'views/fleet_hub_views.xml',
        'views/fleet_document_type_views.xml',
        'views/fleet_document_tag_views.xml',
        'views/fleet_vehicle_inheritance_views.xml',
        'views/fleet_vehicle_model_inheritance_views.xml',
        'views/custom_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
