from odoo import models, fields

class HaemertestEstimate (models.Model):
    _name= "haemer.estimate"
    _description = "Estimate's customer"

    enterprise = fields.Char(string='Enterprise')
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    latitude = fields.Integer(string='Latitude')
    longitude = fields.Integer(string='Longitude')
    past_activity = fields.Char(string='Past Activity')
    future_activity = fields.Char(string='Future Activity')
    remediation_type = fields.Selection([
        ('soil', 'soils'),
        ('choice2', 'choices2'),
        ('choice3', 'choices3'),
    ], required=True, default='soil')
    volume = fields.Integer(string='Volume')
    density = fields.Integer(string='Density')
    humidity = fields.Float(string='Humidity')
    porosity = fields.Float(string='Porosity')



