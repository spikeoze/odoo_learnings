from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class PatientReportWizard(models.TransientModel):
    _name = "assignment.patient.report.wizard"
    _description = "Patient Report Wizard"

    patient_type = fields.Selection(
        string="Patient Type",
        selection=[("kids", "Kids"), ("male", "Male"), ("female", "Female")],
    )

    def print_patient_report(self):
        _logger.info("______________________PATINET_REPORT_____________________")
        domain = []

        if self.patient_type == "male":
            domain += [("gender", "=", "male")]
        if self.patient_type == "female":
            domain += [("gender", "=", "female")]
        if self.patient_type == "kids":
            domain += [("age", "<=", 18)]

        patients = self.env["assignment.patient"].search_read(domain)

        _logger.info(patients)

        data = {"form_data": self.read()[0], "patients": patients}

        return self.env.ref("mu_assignment.patinet_report_action").report_action(
            self, data=data
        )
