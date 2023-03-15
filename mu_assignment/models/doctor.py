# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class AssignmentDoctor(models.Model):
    _name = "assignment.doctor"
    _description = "Assignment Doctor"

    image = fields.Binary(
        string="Doctor Image",
    )

    name = fields.Char(
        string="Name",
        required=True,
    )

    age = fields.Integer(
        string="Age",
    )

    mobile = fields.Char(
        string="Mobile",
    )

    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        default="male",
    )

    speciality = fields.Char(string="Speciality", required=True)
