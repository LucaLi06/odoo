{
    'name': 'Haemers Theme',
    'description': 'Haemers website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
    ],
    'assets':{
            'web.assets_frontend': [
                'theme_haemertest/static/src/scss/styles.scss'
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