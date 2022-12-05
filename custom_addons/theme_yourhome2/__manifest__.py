{
    'name': 'YourHome2 Theme',
    'description': 'YourHome website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': ['views/header.xml',
             'views/footer.xml',],
    'assets':{
        'web.assets_frontend': [
            'theme_yourhome2/static/src/scss/styles.scss'
        ],
        'web._assets_primary_variables': [
            "theme_yourhome2/static/src/scss/primary_variables.scss",
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