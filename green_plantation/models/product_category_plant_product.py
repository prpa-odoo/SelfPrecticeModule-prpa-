from odoo import fields,models

class ProductCategoryPlantProduct(models.Model):
    _name="product.category.plant.product"
    _description="See All Available Plant Products"

    name=fields.Char(required=True)