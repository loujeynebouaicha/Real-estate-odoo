{
    'name': 'Real Estate Management',
    'version': '1.0',
    'author': 'Bouaicha Loujeyne',
    'category': 'Real Estate',
    'summary': 'Manage Real Estate Properties',
    'description': """
        This module allows you to manage real estate properties within Odoo. It provides
        features such as property listings, customer interactions, reports in Excel format,
        and integration with the website and dashboards.
    """,
    'depends': [
        'mail',
        'base',
    ],
    'data': [
        'security/ir.model.access.csv', 'security/security.xml', 'data/mail_template.xml', 'data/sequence_request.xml', 'views/maintenance_wizard_view.xml',
        'views/property_view.xml', 'views/owner_view.xml', 'views/tenant_view.xml', 'views/request_view.xml','report/report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}