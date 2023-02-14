from odoo import fields,models
from datetime import datetime

class ProductVendor(models.Model):
    _name="product.vendor"
    _description="See All Vendor"

    name=fields.Char(required=True,string="Nursery Name")
    contact_no=fields.Char(string="Contact Number")
    address=fields.Text(string="Address")
    email=fields.Char(string="Enter E-mail Id")
    experiance=fields.Integer(readonly=True,string="Experiance Year")
    establish_date=fields.Selection(selection='years_selection',
        string="Establish Year")
    def years_selection(self):
        year_list=[]
        for y in range(datetime.now().year, datetime.now().year + 30):
            year_list.append((str(y), str(y)))
        return year_list
