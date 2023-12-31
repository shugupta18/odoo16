{
    'name': "Helpdesk",
    'version': '1.0.0',
    'category': 'Services/Helpdesk',
    'sequence': -100,
    'author': "Digital Order Technologies Pvt. Limited",
    'website': "https://digitalorder.in",
    'summary': "helpdesk app created by Digital Order Technologies",
    'description': """Helpdesk Management System""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_team_views.xml',
        'views/helpdesk_stage_views.xml',
        'views/helpdesk_sla_policy_views.xml',
        'views/helpdesk_ticket_category_views.xml',
        'views/helpdesk_ticket_source_views.xml',
        'views/helpdesk_tag_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
