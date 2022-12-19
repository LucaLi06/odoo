{
    'name': 'YourHome2 Theme',
    'description': 'YourHome website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': ['views/header.xml',
             'views/footer.xml',
             'views/homepage.xml',
             'views/services_page.xml',
             'views/menus.xml',
             'views/snippets/property-agents.xml',
             'views/snippets/snippets.xml',
             'views/snippets/new-properties.xml',
             'views/snippets/rent_mega_menu.xml',
             'views/snippets/explore-cities.xml',
             'views/yh_cities.xml',
             'security/ir.model.access.csv'],
    'assets':{
        'web.assets_frontend': [
            'theme_yourhome2/static/src/scss/styles.scss',
            'theme_yourhome2/static/src/scss/property-agents.scss',
            'theme_yourhome2/static/src/js/explore-cities.js',
            'theme_yourhome2/static/src/js/explore-cities-option.js'
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