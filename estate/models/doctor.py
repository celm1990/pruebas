from odoo import models, fields
from odoo.exceptions import UserError

class Doctor(models.Model):
    _name = 'doctor'

    name = fields.Char()
    apellido = fields.Char()
    paciente_ids = fields.One2many(comodel_name="paciente", inverse_name="doctor_id")

    def unlink(self):
        return super().unlink()
