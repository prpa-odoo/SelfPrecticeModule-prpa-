from odoo import fields,models

class PlantProduct(models.Model):
    _name="plant.product"
    _description="See All Available Products"

    nursery_name=fields.Char(required=True)
    name=fields.Char(required=True,string="Product Title")
    description=fields.Text(required=True,string="Description")
    product_category=fields.Selection(
        string='Type',required=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )

    product_plant_id=fields.Many2one('product.category.plant',string="Plants")
    product_fertilizer_id=fields.Many2one('product.category.fertilizer',string="Fertilizer")
    product_seeds_id=fields.Many2one('product.category.seeds',string="Seeds")
    product_soil_id=fields.Many2one('product.category.soil',string="Soil")
    product_water_id=fields.Many2one('product.category.water',string="Water")
    product_plantproduct_id=fields.Many2one('product.category.plant.product',string="Plant Product")
    product_tools=fields.Char(string="Tools")
    product_medicine=fields.Char(string="Medicine")
    product_price=fields.Float(string="Price")
    product_img=fields.Image(max_height=70 , max_width=70)
    product_weather_ids=fields.Many2many('product.temperature',string="Weather Condition")
    
    product_quantity=fields.Integer(string="Available Quantity")



