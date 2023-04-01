from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Paciente(models.Model):
    _inherit = 'paciente'
    
    paciente_type = fields.Selection([
        ('public', 'Publico'),
        ('private', 'Privado'),
    ], string='Tipo de paciente')
