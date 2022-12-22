from odoo import models, fields

class HaemertestPartner (models.Model):
    _name= "haemer.partner"
    _description = "Our Partners"

    name = fields.Char(string='Name')
    url = fields.Char(string='URL')
    image = fields.Binary()