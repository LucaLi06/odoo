from odoo import models, fields

class YourTest (models.Model):
    _name= "yh.test"
    _description = "your Test"

    name = fields.Char(string='Name')

