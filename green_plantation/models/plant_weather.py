from odoo import fields,models

class ProductWeather(models.Model):
    _name="product.temperature"
    _description="temperature"

    name=fields.Selection(
        string='Weather',required=True,
        selection = [('summer','Summer'),('winter','Winter'),('rainy','Rainy')],
        )
    weather_temp=fields.Float(string="Temperature")