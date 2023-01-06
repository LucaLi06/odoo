from odoo import models, fields

class HaemertestPatient (models.Model):
    _name= "haemer.patient"
    _description = "Our Patient"

    name = fields.Char(string='Name', required=True)

