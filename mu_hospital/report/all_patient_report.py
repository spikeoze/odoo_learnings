# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AllPatientReport(models.AbstractModel):
    _name = "report.mu_hospital.report_all_patient_list"
    _description = "Patient Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        gender = data.get("form_data").get("gender")
        age = data.get("form_data").get("age")

        domain = []

        if gender:
            domain += [("gender", "=", gender)]

        if age:
            domain += [("age", "=", age)]

        docs = self.env["hospital.patient"].search(domain)

        return {
            "docs": docs,
            "ramla": "mukhtar",
        }


class PatientCard(models.AbstractModel):
    _name = "report.mu_hospital.report_patient_id_card"
    _description = "Patient Report Card"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["hospital.patient"].browse(docids)
      
        return {
            "docs": docs,
        }
