from odoo import models


class PatientCardXlsx(models.AbstractModel):
    _name = "report.mu_hospital.report_patient_id_card_xlsx"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet("Patient ID Cards")
        sheet.set_column("A:A", 10)
        bold = workbook.add_format({"bold": True})
        left = workbook.add_format({"align": "left"})
        center = workbook.add_format({"bold": True, "align": "center", "bg_color":"orange"})

        row = 1
        col = 0
        for obj in patients:
            row += 1
            # One sheet by partner
            sheet.merge_range("A1:C1", "All Patients", center)
            sheet.write(1, 0, "Reference", bold)
            sheet.write(row, col, obj.reference)
            sheet.write(1, 1, "Name", bold)
            sheet.write(row, col + 1, obj.name)
            sheet.write(1, 2, "Age", bold)
            sheet.write(row, col + 2, obj.age, left)
