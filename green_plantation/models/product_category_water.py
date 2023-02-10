from odoo import fields,models

class ProductCategoryWater(models.Model):
    _name="product.category.water"
    _description="How Much Water Plant Need"

    name=fields.Char(required=True)

