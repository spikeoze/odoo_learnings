# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class AssignmentService(models.Model):
    _name = "assignment.service"
    _description = "Assignment Service"

    name = fields.Char(
        string="Name",
        required=True,
    )

    service_type = fields.Selection(
        string="Service Type",
        selection=[
            ("laboratory", "Laboratory"),
            ("dermatology", "Dermatology"),
            ("surgery", "Surgery"),
            ("radiology", "Radiology"),
        ],
        required=True,
    )

    price = fields.Float(string="Price", required=True)

    
