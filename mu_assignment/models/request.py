# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class AssignmentRequest(models.Model):
    _name = "assignment.request"
    _description = "Assignment Doctor Request"
    _rec_name = "patient_id"

    patient_id = fields.Many2one(
        string="Patient",
        required=True,
        comodel_name="assignment.patient",
    )

    age = fields.Integer(
        related="patient_id.age",
        readonly=True,
        string="Age",
    )

    date = fields.Date(
        string="Date",
        default=fields.Date.context_today,
    )

    doctor_id = fields.Many2one(
        string="Doctor",
        required=True,
        comodel_name="assignment.doctor",
    )

    # service_id = fields.Many2one(
    #     string='Service',
    #     comodel_name='assignment.service',
    # )

    # Relationship with service
    service_ids = fields.One2many(
        string="Request",
        comodel_name="assignment.request.line",
        inverse_name="request_id",
    )


class AssignmentRequestLine(models.Model):
    _name = "assignment.request.line"
    _description = "Request Line"

    service_id = fields.Many2one(
        string="Service",
        required=True,
        comodel_name="assignment.service",
        ondelete="restrict",
    )

    service_type  = fields.Selection(
        string="Service Type",
        related="service_id.service_type",
        readonly=True,
    )

    price = fields.Float(
        related="service_id.price",
        string="price",
    )

    request_id = fields.Many2one(
        string="Request",
        comodel_name="assignment.request",
    )
