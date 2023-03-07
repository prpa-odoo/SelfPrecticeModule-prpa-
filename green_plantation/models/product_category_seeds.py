from odoo import fields,models,api

class ProductCategorySeeds(models.Model):
    _name="product.category.seeds"
    _description="See All Available Products Seeds"

    name=fields.Char(required=True)

    seeds_ids = fields.One2many('plant.product','seeds_type_id')

    offer_ids = fields.One2many('plant.offer','offer_id')
    offer_count = fields.Integer(compute="_compute_offer")

    @api.depends('offer_ids')
    def _compute_offer(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids) 
            else:
                record.offer_count = 0
