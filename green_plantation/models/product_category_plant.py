from odoo import fields,models

class ProductCategoryPlant(models.Model):
    _name="product.category.plant"
    _description="See All Available Products Category"

    name=fields.Char(required=True)