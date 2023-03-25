from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class DoctorRequestReportWizard(models.TransientModel):
    _name = "doctor.request.report.wizard"
    _description = "Doctor Request Report Wizard"

    patient_id = fields.Many2one(
        string="Patient",
        comodel_name="assignment.patient",
        ondelete="restrict",
    )

    date_from = fields.Date(
        string="Date From",
    )

    date_to = fields.Date(
        string="Date to",
    )

    def doctor_request_report(self):
        domain = []

        if self.patient_id:
            domain += [("patient_id", "=", self.patient_id.id)]
        if self.date_from:
            domain += [("date", ">=", self.date_from)]
        if self.date_to:
            domain += [("date", "<=", self.date_to)]

        requests = self.env["assignment.request"].search_read(domain)
        # _logger.info("----------------------------------")

        # for x in requests:
        #     for a in x["service_ids"]:
        #        services = self.env['assignment.request'].browse(a)
        #        for y in services['service_ids']:
        #            _logger.info(y['service_type'])
                   
                   
                   
        data = {
            "form_data": self.read()[0],
            "requests": requests,
        }
                
            
            
        return self.env.ref("mu_assignment.request_report_wizard_action").report_action(
            self, data=data
        )
