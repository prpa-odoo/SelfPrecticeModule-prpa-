from odoo import fields,models

class PlantMedicine(models.Model):
    _name="plant.doctor"
    _description="plant doctor"

    name=fields.Char(required=True)
    # phone_no=fields.Char()
    # prescription=fields.Char()
    # user=fields.selection(
    #     selection=[('doctor','Doctor'),('in_user','Internal User')]
    # )
    