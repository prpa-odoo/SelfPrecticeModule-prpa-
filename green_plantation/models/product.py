from odoo import fields,models

class Product(models.Model):
    _name="products"
    _description="See All Available Products"

    name=fields.Char(required=True)