from odoo import fields,models

class PlantMedicine(models.Model):
    _name="plant.medicine"
    _description="plant medicine"

    name=fields.Char(required=True)

    medicine_ids = fields.One2many('plant.product','medicine_type_id')
