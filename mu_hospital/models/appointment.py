# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError


# Modal
class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "reference"

    reference = fields.Char(
        string="Reference",
        readonly=True,
        required=True,
        copy=False,
        default=lambda self: _("New"),
    )

    patient_id = fields.Many2one(
        "hospital.patient", string="Patient", tracking=True, required=True
    )

    doctor_id = fields.Many2one(
        string="Doctor",
        tracking=True,
        required=True,
        comodel_name="hospital.doctor",
    )

    age = fields.Integer(string="Age", related="patient_id.age", tracking=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        required=True,
        default="male",
        tracking=True,
    )

    description = fields.Text(string="Description", tracking=True)

    date_appointment = fields.Date(string="Date", default=fields.Date.context_today)

    date_checkup = fields.Datetime(string="Checkup Time")

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Canceled"),
        ],
        string="Status",
        default="draft",
        tracking=True,
    )

    prescription = fields.Text(
        string="prescription",
    )

    prescription_line_ids = fields.One2many(
        "appointment.prescription.lines",
        "appointment_id",
        string="prescription_line",
    )

    # Status Functions
    def action_confirm(self):
        self.state = "confirm"

    def action_draft(self):
        self.state = "draft"

    def action_cancel(self):
        self.state = "cancel"

    def action_done(self):
        self.state = "done"

    # Url Function
    def action_url(self):
        return {
            "target": "new",
            "type": "ir.actions.act_url",
            "url": "https://github.com/spikeoze",
        }

    # Overriding the create method
    @api.model
    def create(self, values):
        if not values.get("description"):
            values["description"] = "New Appointment"

        if values.get("reference", _("New")) == _("New"):
            values["reference"] = self.env["ir.sequence"].next_by_code(
                "hospital.appointment"
            ) or _("New")

        result = super(HospitalAppointment, self).create(values)

        return result

    # On change Function: typical onChange method.
    # @api.onchange('')

    @api.onchange("patient_id")
    def _onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.description:
                self.description = self.patient_id.description
        else:
            self.gender = ""

    # Unlink method controls the delete functionality

    def unlink(self):
        if self.state == "done":
            raise ValidationError(
                _("You cannot delete record %s as it is in done state" % self.reference)
            )
        result = super(HospitalAppointment, self).unlink()
        return result


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines "

    name = fields.Char(string="Name", tracking=True, required=True)
    qty = fields.Integer(string="Quantity", tracking=True, required=True)

    appointment_id = fields.Many2one(
        string="Appointment",
        comodel_name="hospital.appointment",
    )
