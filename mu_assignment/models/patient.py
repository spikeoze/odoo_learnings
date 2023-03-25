# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
import warnings
from odoo.exceptions import UserError
from datetime import date, timedelta
import logging

_logger = logging.getLogger(__name__)


class AssignmentPatient(models.Model):
    _name = "assignment.patient"
    _description = "Assignment Patient"

    image = fields.Binary(
        string="Patient Image",
    )

    name = fields.Char(
        string="Name",
        required=True,
    )

    age = fields.Integer(
        string="Age",
    )

    birth_date = fields.Date(
        string="Date Of Birth",
        default=fields.Date.context_today,
    )

    mobile = fields.Char(
        string="Mobile",
    )

    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        default="male",
    )

    def getActionId(self):
        _logger.info(self._context)


    @api.onchange("age")
    def _onchange_age(self):
        if self.age:
            today = date.today()
            birthday = today - timedelta(days=(self.age * 365.2425))
            self.birth_date = birthday

    # def unlink(self):
    #     """
    #     Delete all record(s) from recordset
    #     return True on success, False otherwise

    #     @return: True on success, False otherwise

    #     #TODO: process before delete resource
    #     """
    #     for patient in self:
    #         if patient.name == "ramla" or "Ramla":
    #             raise UserError("You cannot delete Ramla")
    #     result = super(AssignmentPatient, self).unlink()

    #     return result

    def testMethod(self):
        # res = self.env["assignment.patient"].search_read([('age', "<", 25)])

        # fields = self.env["assignment.patient"].fields_get()

        res = self.env["assignment.patient"].browse([1, 2, 3])
        for x in res:
            data = {
                "name": x["name"],
                "age": x["age"],
                "gender": x["gender"],
                "mobile": x["mobile"],
            }
            _logger.info(data)
            _logger.info("___________________________________________________--")
