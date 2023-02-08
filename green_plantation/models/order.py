from odoo import fields,models

class Order(models.Model):
    _name="orders"
    _description="See All Orders"

    name=fields.Char(required=True)
