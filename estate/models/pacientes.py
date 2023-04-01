from odoo import models, fields
from odoo.exceptions import UserError

class Paciente(models.Model):
    _name = 'paciente'

    name = fields.Char()
    doctor_id = fields.Many2one(comodel_name="doctor")
    doctor_ids = fields.Many2many(comodel_name="doctor", string="Doctores")

    def crear_doctor(self):
        DoctorModel = self.env["doctor"]
        new_doctor = DoctorModel.create([{
            "name": "NUEVO DOCTOR"
        }])
        self.write({
            "doctor_id": new_doctor.id,
            "doctor_ids": [(4, new_doctor.id)],
        })
        return True

    def cambiar_doctor(self):
        self.doctor_id.write({"name": "DOCTOR CAMBIADO"})
        return True

    def buscar_cambiar_doctor(self):
        DoctorModel = self.env["doctor"]
        doctores_encontrados = DoctorModel.search([
            ("name", "=", "Doctor 27"),
            
        ])
        doctores_encontrados.write({"name": "NOMBRE CAMBIADO 30"})
        return True

    def eliminar_doctor(self):
        DoctorModel = self.env["doctor"]
        doctores_encontrados = DoctorModel.search([])
        doctores_encontrados.unlink()
        return True

    def remove_doctor(self):
        self.write({
            "doctor_ids": [(6, 0, [])],
        })
        return True
    
    def vincular_doctor(self):
        DoctorModel = self.env["doctor"]
        doctores_encontrados = DoctorModel.search([])
        self.write({
            "doctor_ids": [(6, 0, doctores_encontrados.ids)],
        })
        return True
