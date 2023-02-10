from odoo import fields,models

class ProductCategorySeeds(models.Model):
    _name="product.category.seeds"
    _description="See All Available Products Seeds"

    name=fields.Char(required=True)