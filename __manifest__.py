# -*- coding: utf-8 -*-
# Part of Mediod Technologies.
{
    "name":   "Realstate Management",
    "author": "Muhammad Baqir",
    "support": " ",
    "license": "OPL-1",
    "category": "Pre Internship",
    "summary": """
    Simple Realstate Management Application,
    """,
    "description": """
    Simple Realstate Module
    """,
    "version": "1.0.0",
    "depends": [
        "theme_real_estate",
    ],
    "application": True,
    'installable': True,
    'auto_install': False,
    'application': False,
    "data": [
        "data/realstate_data.xml",
        "views/estate_property_views.xml",
        "views/property_units_views.xml",
        "views/menus.xml",
        'security/ir.model.access.csv',
    ],
    "auto_install": False,
    "installable": True,
}
