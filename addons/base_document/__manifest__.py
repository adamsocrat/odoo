{
    'name': "Base Document",
    'summary': 'This module adds additional documents for external reports and manipulates email templates',
    'author': 'ycs',
    'category': 'Base',
    'version': '17.0.0.5',
    'depends': [
        'l10n_din5008',
        'mail',
    ],
    'data': [
        'views/report_templates.xml',
        'views/auth_signup_templates_email_override.xml',
        'views/invoice_template.xml',
        'data/report_layout.xml',
        'views/webclient_templates_override.xml',
    ],
    # 'assets': {
    #     'web.report_assets_common': [
    #         'base_document/static/src/**/*',
    #     ],
    # },
    'installable': True,
    'application': False,
    'auto_install': True,
}
