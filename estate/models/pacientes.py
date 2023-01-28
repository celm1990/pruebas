from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Paciente(models.Model):
    _name = 'paciente'

    name = fields.Char()
    price_unit = fields.Float(string="Precio Unitario")
    product_qty = fields.Float(strig="Cantidad")
    subtotal = fields.Float(strig="Subtotal", compute="_compute_subtotal", store=True)
    doctor_id = fields.Many2one(comodel_name="doctor")
    apellido_doctor = fields.Char()
    doctor_ids = fields.Many2many(comodel_name="doctor", string="Doctores")

    _sql_constraints = [
        (
            "doctor_unique",
            "unique(doctor_id)",
            "El doctor no se puede repetir por paciente!",
        )
    ]

    @api.constrains('price_unit')
    def _check_price_unit(self):
        for record in self:
            if record.price_unit <0:
                raise ValidationError(f"El precio unitario debe ser mayor a cero, del paciente: {record.name}")
        
    @api.onchange("doctor_id")
    def _onchange_doctor_id(self):
        self.apellido_doctor = self.doctor_id.apellido

    @api.depends("price_unit", "product_qty")
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.price_unit * record.product_qty


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
