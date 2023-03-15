# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AllPatientReport(models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Print Patient Report Wizard"

    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female"), ("other", "Other")],
    )

    age = fields.Integer(
        string="Age",
    )

    def action_print_report(self):
        data = {
            "form_data": self.read()[0],
        }

        return self.env.ref("mu_hospital.report_all_patient_action").report_action(
            self, data=data
        )
