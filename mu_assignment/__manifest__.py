# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Assignment Module",
    "version": "1.1",
    "summary": "For solving assignments",
    "sequence": 3,
    "description": """Assignment Module""",
    "category": "Productivity/productivity",
    "website": "https://www.mukhtar-amin.tk",
    "depends": [],
    "data": [
        "security/ir.model.access.csv",
        "views/patient_view.xml",
        "views/doctor_view.xml",
        "views/service_view.xml",
        "views/request_view.xml",
        "report/report.xml",
        "report/patinet_card_template.xml",
        "report/doctor_card_template.xml",
        "report/doctor_request_template.xml",
    ],
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
