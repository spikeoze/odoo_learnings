# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Doctor"
    _rec_name = "doctor_name"

    image = fields.Binary(
        string="Patient Image",
    )

    doctor_name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
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

    appointment_count = fields.Integer(
        string="Appointment Count", tracking=True, compute="_compute_appointment_count"
    )

    active = fields.Boolean(string="Active", default=True)

    # Copy method controlles the duplicate functionality
    # @api.multi
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get("doctor_name"):
            default["doctor_name"] = _("%s (Copy)", self.doctor_name)
            default["description"] = "Copied Record"
        result = super(HospitalDoctor, self).copy(default)

        return result

    def _compute_appointment_count(self):
        for record in self:
            appointment_count = self.env["hospital.appointment"].search_count(
                [("doctor_id", "=", record.id)]
            )
            record.appointment_count = appointment_count
