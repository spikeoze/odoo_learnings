# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class DoctorRequestWizard(models.TransientModel):
    _name = "doctor.request.wizard"
    _description = "Doctor Request Wizard"

    @api.model
    def default_get(self, fields):
        res = super(DoctorRequestWizard, self).default_get(fields)
        if self._context.get("active_id"):
            res["patient_id"] = self._context.get("active_id")

        return res

    patient_id = fields.Many2one(
        string="Patient",
        required=True,
        comodel_name="assignment.patient",
    )

    age = fields.Integer(string="Age", related="patient_id.age", readonly=True)

    doctor_id = fields.Many2one(
        string="Doctor",
        required=True,
        comodel_name="assignment.doctor",
    )

    date = fields.Date(
        string="Date",
        default=fields.Date.context_today,
    )

    service_ids = fields.One2many(
        string="Request",
        comodel_name="request.line.wizard",
        inverse_name="request_id",
    )

    def request_doctor(self):
        request_lines = []
        for line in self.service_ids:
            request_lines.append(
                (
                    0,
                    0,
                    {
                        "service_id": line.service_id.id,
                        "service_type": line.service_type,
                        "price": line.price,
                    },
                )
            )

        values = {
            "patient_id": self.patient_id.id,
            "age": self.age,
            "doctor_id": self.doctor_id.id,
            "date": self.date,
            "service_ids": request_lines,
        }

        _logger.info(values)

        doctor_request = self.env["assignment.request"].create(values)

        return {
            "name": _("Doctor Request"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "assignment.request",
            "res_id": doctor_request.id,
        }


class RequestLineWizard(models.TransientModel):
    _name = "request.line.wizard"
    _description = "Request Line"

    service_id = fields.Many2one(
        string="Service",
        required=True,
        comodel_name="assignment.service",
        ondelete="restrict",
    )

    service_type = fields.Selection(
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
        comodel_name="doctor.request.wizard",
    )
