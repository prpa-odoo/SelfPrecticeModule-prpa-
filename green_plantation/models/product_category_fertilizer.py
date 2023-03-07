from odoo import fields,models,api

class ProductCategoryFertilizer(models.Model):
    _name="product.category.fertilizer"
    _description="See All Available Products Fertilizer"

    name=fields.Char(required=True)

    fertilizer_ids = fields.One2many('plant.product','fertilizer_type_id')

    offer_ids = fields.One2many('plant.offer','offer_id')
    offer_count = fields.Integer(compute="_compute_offer")

    @api.depends('offer_ids')
    def _compute_offer(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids) 
            else:
                record.offer_count = 0
