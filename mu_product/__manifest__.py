# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Product Sale",
    "version": "1.1",
    "summary": "Product Sale Software",
    "sequence": 2,
    "description": """Product Sale Software""",
    "category": "Productivity/productivity",
    "website": "https://www.mukhtar-amin.tk",
    "depends": ["product"],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/product.xml",
        "views/product_inherit.xml",
    ],
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
