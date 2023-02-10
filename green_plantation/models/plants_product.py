from odoo import fields,models

class PlantProduct(models.Model):
    _name="plant.product"
    _description="See All Available Products"

    nursery_name=fields.Char(required=True)
    name=fields.Char(required=True,string="Project Title")
    description=fields.Text(required=True,string="Description")
    product_category=fields.Selection(
        string='Type',required=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )

    product_plant_id=fields.Char(string="Plants")
    product_fertilizer_id=fields.Char(string="Fertilizer")
    product_seeds_id=fields.Char(string="Seeds")
    product_soil_id=fields.Char(string="Soil")
    product_water_id=fields.Char(string="Water")
    product_plantproduct_id=fields.Char(string="Plant Product")
    product_tools=fields.Char(string="Tools")
    product_medicine=fields.Char(string="Medicine")
    product_price=fields.Float(string="Price")
    product_img=fields.Image()