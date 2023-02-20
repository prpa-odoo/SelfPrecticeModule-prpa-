from odoo import fields,models

class Order(models.Model):
    _name="order.orders"
    _description="See All Orders"

    name=fields.Char(required=True)
    product=fields.Char(string="product")
    description=fields.Char(string="description")
    quantity=fields.Integer()
    unit_price=fields.Integer()
    taxes=fields.Integer()
    sub_total=fields.Integer()
    offer=fields.Char()

    order_ids = fields.One2many("plant.product", "order_type_id")
