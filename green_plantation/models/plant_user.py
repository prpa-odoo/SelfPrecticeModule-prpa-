from odoo import fields,models

class PlantUser(models.Model):
   _name = "plant.user"
   _description = "User Details"

   uname = fields.Char(required=True,string="UserName")
   address=fields.Text(string="Address")
   
   phone_no=fields.Char(string="PhoneNo")
   email=fields.Char(string="Email")
   user_role=fields.Selection(
      string="Type Of User",
      selection=[('customer','Customer'),('farmer','Farmar'),('caretaker','Caretaker')]
   )

   work_place_id=fields.Many2one('product.vendor',string="Nursery Place")

   caretaker_work_place=fields.Text(string="Reason To Leave Previous Work Space")
   add_caretaker=fields.Text(string="Address Of Previous Workspace")

   experiance=fields.Integer(string="Experiance")

   country_id = fields.Many2one('res.country', string='Country')
   state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")


