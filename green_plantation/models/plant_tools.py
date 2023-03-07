from odoo import fields,models,api

class PlantTools(models.Model):
    _name="plant.tools"
    _description="plant tools"

    name=fields.Char(required=True)
    tools_img=fields.Image()

    tools_ids = fields.One2many('plant.product','tools_type_id')

    offer_ids = fields.One2many('plant.offer','offer_id')
    offer_count = fields.Integer(compute="_compute_offer")

    @api.depends('offer_ids')
    def _compute_offer(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids) 
            else:
                record.offer_count = 0
