{
    'name': 'YourHome2 Theme',
    'description': 'YourHome2 website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/services_page.xml',
        'views/snippets/property-agents.xml',
        'views/snippets/new-properties.xml',
        'views/snippets/explore-cities.xml',
        'views/snippets/snippets.xml',
        'views/yh_cities.xml',
        'views/website_test.xml',
    ],
    'assets':{
        'web.assets_frontend': [
            'theme_yourhome2/static/src/scss/styles.scss',
            'theme_yourhome2/static/src/scss/property-agents.scss',
            'theme_yourhome2/static/src/js/explore-cities.js',
            'theme_yourhome2/static/src/js/explore-cities-options.js',
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