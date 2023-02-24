from odoo import fields,models,api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class ProductVendor(models.Model):
    _name="product.vendor"
    _description="See All Vendor"

    name=fields.Char(required=True,string="Nursery Name")
    contact_no=fields.Char(string="Contact Number")
    address=fields.Text(string="Address")
    email=fields.Char(string="Enter E-mail Id")
    available=fields.Boolean()
    experiance=fields.Integer(compute='_compute_year',readonly=True,string="Experiance Year")
    establish_date=fields.Selection(selection='years_selection',
        string="Establish Year")
    def years_selection(self):
        year_list=[]
        for y in range(datetime.now().year-23, datetime.now().year):
            year_list.append((str(y), str(y)))
        return year_list

    @api.depends('establish_date')
    def _compute_year(self):
        for record in self:
            record.experiance = fields.date.today().year-int(record.establish_date)
           


   