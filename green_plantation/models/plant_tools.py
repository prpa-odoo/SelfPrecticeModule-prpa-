from odoo import fields,models

class PlantTools(models.Model):
    _name="plant.tools"
    _description="plant tools"

    name=fields.Char(required=True)
    tools_img=fields.Image()