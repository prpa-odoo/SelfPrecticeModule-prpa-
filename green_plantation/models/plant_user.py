from odoo import fields,models

class PlantUser(models.Model):
   _name = "plant.user"
   _description = "User Details"

   uname = fields.Char(required=True,string="UserName")
   address=fields.Text(string="Address")
   phone_no=fields.Integer(string="PhoneNo")
   email=fields.Char(string="Email")
   user_role=fields.Selection(
      string="Select User",
      selection=[('customer','Customer'),('farmer','Farmar'),('visitor','Visitor'),('caretaker','Caretaker')]
   )
