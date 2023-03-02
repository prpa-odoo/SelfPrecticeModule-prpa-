from odoo import fields,models

class PlantTools(models.Model):
    _name="plant.tools"
    _description="plant tools"

    name=fields.Char(required=True)
    tools_img=fields.Image()

    tools_ids = fields.One2many('plant.product','tools_type_id')