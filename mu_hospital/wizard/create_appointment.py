# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "create appointment wizard"

    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        if self._context.get("active_id"):
            res["patient_id"] = self._context.get("active_id")
        return res

    date_appointment = fields.Date(string="Date", required=False)

    patient_id = fields.Many2one(
        "hospital.patient", string="Patient", tracking=True, required=True
    )

    doctor_id = fields.Many2one(
        string="Doctor",
        comodel_name="hospital.doctor",
    )

    def create_appointment_action(self):
        vals = {
            "patient_id": self.patient_id.id,
            "date_appointment": self.date_appointment,
            "doctor_id": self.doctor_id.id
        }
        appointment_rec = self.env["hospital.appointment"].create(vals)
        return {
            "name": _("Appointment"),
            "type": "ir.actions.act_window",
            # "view_type": "form",
            "view_mode": "form",
            "res_model": "hospital.appointment",
            "res_id": appointment_rec.id,
        }

    def view_appointment_action(self):
        action = self.env.ref("mu_hospital.action_hospital_appointment").read()[0]
        action["domain"] = [("patient_id", "=", self.patient_id.id)]

        return action

        # action = self.env["ir.actions.actions"]._for_xml_id(
        #     "mu_hospital.action_hospital_appointment"
        # )
        # action["domain"] = [("patient_id", "=", self.patient_id.id)]

        # return action

        # return {
        #     "name": _("View Appointments"),
        #     "type": "ir.actions.act_window",
        #     "view_mode": "tree",
        #     "res_model": "hospital.appointment",
        #     "res_id": self.id,
        #     "domain": [("patient_id", "=", self.patient_id.id)],
        # }
