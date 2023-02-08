from odoo import fields,models

class PlantUser(models.Model):
    _name = "plant.user"
    _description = "User Details"

    name = fields.Char(required=True)
