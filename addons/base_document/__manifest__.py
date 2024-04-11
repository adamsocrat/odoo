{
    'name': "Base Document",
    'summary': 'This module adds additional documents for external reports.',
    'author': 'Ben',
    'category': 'Base',
    'version': '17.0.0.1.1',
    'depends': ['l10n_din5008'],
    'data': [
        'views/report_templates.xml',
        'views/invoice_template.xml',
        'data/report_layout.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'base_document/static/src/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
