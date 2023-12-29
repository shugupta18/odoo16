{
    'name': "Helpdesk",
    'version': '1.0.0',
    'category': 'Services/Helpdesk',
    'sequence': -100,
    'author': "Digital Order Technologies Pvt. Limited",
    'website': "https://digitalorder.in",
    'summary': "helpdesk app created by Digital Order Technologies",
    'description': """Helpdesk Management System""",
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
