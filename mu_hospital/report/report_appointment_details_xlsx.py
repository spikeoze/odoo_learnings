from odoo import models

import logging

_logger = logging.getLogger(__name__)


class AppointmentDetailsXlsx(models.AbstractModel):
    _name = "report.mu_hospital.report_appointment_details_xlsx"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet("Appointment Details")
        sheet.set_column("A:A", 10)
        sheet.set_column("B:B", 20)
        bold = workbook.add_format({"bold": True})
        header = workbook.add_format({"align": "center", "bold": True})

        date_from = data.get("form_data").get("date_from")
        date_to = data.get("form_data").get("date_to")

        sheet.write(2, 0, "Date From", bold)
        sheet.write(2, 1, date_from)
        sheet.write(3, 0, "Date To", bold)
        sheet.write(3, 1, date_to)

        sheet.write(5, 0, "Reference", bold)
        sheet.write(5, 1, "Name", bold)
        sheet.merge_range("A1:B1", "Appointment Detail", header)
        row = 5
        col = 0
        for appointment in data["appointments"]:
            row += 1
            # One sheet by partner
            sheet.write(row, col, appointment["reference"])
            sheet.write(row, col + 1, appointment["patient_id"][1])
