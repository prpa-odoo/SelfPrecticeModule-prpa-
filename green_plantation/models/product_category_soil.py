from odoo import fields,models

class ProductCategorySoil(models.Model):
    _name="product.category.soil"
    _description="See All Available Products Soil"

    name=fields.Char(required=True)