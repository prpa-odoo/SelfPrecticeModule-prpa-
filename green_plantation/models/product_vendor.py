from odoo import fields,models

class ProductVendor(models.Model):
    _name="product.vendor"
    _description="See All Vendor"

    name=fields.Char(required=True,string="Nursery Name")
    contact_no=fields.Integer(string="Contact Number")
    address=fields.Text(string="Enter Address")
    email=fields.Char(string="Enter E-mail Id")
    experiance=fields.Integer(required=True,string="Experiance Year")
