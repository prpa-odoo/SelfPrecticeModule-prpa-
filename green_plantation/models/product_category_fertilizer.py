from odoo import fields,models

class ProductCategoryFertilizer(models.Model):
    _name="product.category.fertilizer"
    _description="See All Available Products Fertilizer"

    name=fields.Char(required=True)

    fertilizer_ids = fields.One2many('plant.product','fertilizer_type_id')