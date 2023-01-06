from odoo import models, fields

class YourPatient (models.Model):
    _name= "yh.patient"
    _description = "your Patient"

    name = fields.Char(string='Name')

