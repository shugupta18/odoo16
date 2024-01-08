{
    'name': "Fleet - MOD",
    'summary': """Fleet module customization by dotpl""",
    'description': """Fleet module customization by dotpl""",
    'author': "DOTPL",
    'website': "https://digitalorder.in",
    'category': 'Fleet',
    'version': '1.0',
    'sequence': -200,

    'depends': ['fleet'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/custom_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
