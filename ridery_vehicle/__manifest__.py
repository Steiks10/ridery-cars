# -*- coding: utf-8 -*-
{
    "name": "Ridery Vehicle Management",
    "version": "1.1",
    'author': "Steiker Mieles",
    "license": "OPL-1",
    "website": "",
    'contributors': [
        'Steiker Mieles <steiker.m2002@gmail.com>',
    ],
    "category": 'Generic Modules/Ridery',
    "depends": ['base', 'contacts', 'fleet', 'stock', 'ridery_log'],
    'data': [
        "data/sequence.xml",
        "views/fleet_vehicle_inherit_form.xml",
        "views/res_partner_inherit_form.xml",
        "views/fleet_vehicle_stock_location_graph.xml",
        "views/fleet_vehicle_inherit_search.xml",
        "views/driver_action_view.xml",
        "views/fleet_config.xml",
        "views/menu_item.xml",
    ],
    'installable': True,
}
