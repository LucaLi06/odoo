{
    'name': 'Haemers Theme',
    'description': 'Haemers website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/snippets/home-snippet.xml',
        'views/snippets/snippets.xml',
        'views/ht_partner.xml',
        'security/ir.model.access.csv',
        'views/snippets/display-partner.xml',
        'views/website_form.xml',
        'views/estimate_form.xml',
        'views/thx_estimate.xml',
        'views/ht_estimate.xml',

    ],
    'assets':{
            'web.assets_frontend': [
                'theme_haemertest/static/src/scss/styles.scss',
                'theme_haemertest/static/src/js/display-partner.js',

            ],
            'web._assets_primary_variables': [
                "theme_haemertest/static/src/scss/primary_variables.scss",
            ]
        },
    'images': [
    ],
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}