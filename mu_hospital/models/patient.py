# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

# Modal
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"
    _order = "reference desc"

    # Default get function (Give default values to fields)
    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        if not res.get("gender"):
            res["gender"] = "male"

        return res

    reference = fields.Char(
        string="Reference",
        readonly=True,
        required=True,
        copy=False,
        default=lambda self: _("New"),
    )

    image = fields.Binary(
        string="Patient Image",
    )

    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        required=True,
        # default="male",
        tracking=True,
    )
    description = fields.Text(string="Description", tracking=True)

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


    responsible_id = fields.Many2one("res.partner", string="responsible")

    appointment_count = fields.Integer(
        string="Appointment Count", tracking=True, compute="_compute_appointment_count"
    )

    appointment_ids = fields.One2many(
        "hospital.appointment", "patient_id", string="Appointment"
    )
    
       
    
   

    # Computed Field Function
    # @api.depends("depends")
    def _compute_appointment_count(self):
        # patients = self.env['hospital.patient'].search_read([])
        # _logger.info(patients);

        
        for record in self:
            appointment_count = self.env["hospital.appointment"].search_count(
                [("patient_id", "=", record.id)]
            )
            record.appointment_count = appointment_count

    # Status Functions
    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    # Overriding the create method
    @api.model
    def create(self, values):
        if not values.get("description"):
            values["description"] = "New Patient"

        if values.get("reference", _("New")) == _("New"):
            values["reference"] = self.env["ir.sequence"].next_by_code(
                "hospital.patient"
            ) or _("New")

        result = super(HospitalPatient, self).create(values)

        return result

    @api.constrains("name")
    def _check_name(self):
        for record in self:
            patient = self.env["hospital.patient"].search(
                [("name", "=", record.name), ("id", "!=", record.id)]
            )
            if patient:
                raise ValidationError(_("%s already exists" % patient))

    @api.constrains("age")
    def _check_age(self):
        for record in self:
            if record.age == 0:
                raise ValidationError(_("Age connot be 0"))

    def name_get(self):
        result = []
        for record in self:
            name = record.reference + " " + record.name
            result.append((record.id, name))
        return result

    def action_open_appointment(self):
        return {
            "name": "Appointment",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "hospital.appointment",
            "domain": [("patient_id", "=", self.id)],
        }
