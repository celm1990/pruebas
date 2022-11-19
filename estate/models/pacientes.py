from odoo import models, fields

class Paciente(models.Model):
    _name = 'paciente'

    name = fields.Char()
