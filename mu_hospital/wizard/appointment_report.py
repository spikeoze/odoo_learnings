# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AppointmentReport(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Report Wizard"

    patient_id = fields.Many2one(
        "hospital.patient",
        string="Patient",
    )

    date_from = fields.Date(string="Date From")

    date_to = fields.Date(string="Date To")

    def action_print_report(self):
        domain = []

        if self.patient_id:
            domain += [("patient_id", "=", self.patient_id.id)]
        if self.date_from:
            domain += [("date_appointment", ">=", self.date_from)]
        if self.date_to:
            domain += [("date_appointment", "<=", self.date_to)]

        appointments = self.env["hospital.appointment"].search_read(domain)

        # _logger.info(appointments)

        data = {
            "form_data": self.read()[0],
            "appointments": appointments,
        }

        return self.env.ref("mu_hospital.report_appointment_action").report_action(
            self, data=data
        )

    def action_print_excel_report(self):
        domain = []

        if self.patient_id:
            domain += [("patient_id", "=", self.patient_id.id)]
        if self.date_from:
            domain += [("date_appointment", ">=", self.date_from)]
        if self.date_to:
            domain += [("date_appointment", "<=", self.date_to)]

        appointments = self.env["hospital.appointment"].search_read(domain)

        data = {
            "form_data": self.read()[0],
            "appointments": appointments,
        }

        return self.env.ref(
            "mu_hospital.report_appointment_details_xlsx"
        ).report_action(self, data=data)
