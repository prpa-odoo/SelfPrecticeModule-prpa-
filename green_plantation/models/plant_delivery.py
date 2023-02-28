from odoo import models,fields

class PlantDelivery(models.Model):
    _name = "plant.delivery"
    _description = "Plant Delivery Time"

    group_id = fields.Char(string="Country Group")
    state_id = fields.Many2many('res.country.state')
    delivery = fields.Char()