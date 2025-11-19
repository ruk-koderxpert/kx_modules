{
    'name' : 'Approvals Teams',
    'version' : '18.0.1.0.2',
    'summary': '''This module enables multi-level approval processes across various models in Odoo, 
        allowing users to define custom teams and approvers for streamlined management of approvals in different business processes.
    ''',
    'description': """The Approvals Teams module provides functionality for creating approval teams within Odoo, 
        allowing businesses to define custom approvers and set up multi-level approval processes for various models such as sales orders, purchase orders, and invoices.
        With this module, you can:
        Set up teams with specific approvers to handle approvals.
        Customize the sequence of approval steps and assign team leaders.
        Assign approval responsibilities based on company or model.
        Define approval validation thresholds based on amounts.
        Easily manage and track team members and approvers through user-friendly forms and kanban views.
        This module helps to streamline and enforce approval workflows, improving business process control and reducing errors.
    """,
    'author': 'KoderXpert Technologies LLP',
    'company': 'KoderXpert Technologies LLP',
    'maintainer': 'KoderXpert Technologies LLP',
    'website': 'https://koderxpert.com',
    'category': 'Productivity',
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/team_view.xml',
        'views/approval_view.xml',
        ],
    'installable':True,
    'application':True,
    'auto_install':False,
    'license': 'LGPL-3',
    'images':['static/description/team_approval.gif'],
}
