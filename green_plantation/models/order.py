from odoo import fields,models

class Order(models.Model):
    _name="order.orders"
    _description="See All Orders"

    name=fields.Char(required=True)
    description=fields.Char(string="description")
    quantity=fields.Integer()
    unit_price=fields.Integer()
    taxes=fields.Integer()
    sub_total=fields.Integer()
    offer=fields.Char()

    product_ids=fields.Many2many("plant.product",string="product")
    order_ids = fields.One2many("plant.product", "order_type_id")


    # def action_send_email(self):
    #     mail_template = self.env.ref('test_email.email_template')
    #     mail_template.send_mail(self.id, force_send=True)
            
    # def action_cancle(self):
    #     for record in self:
    #         if record.state == "sold":
    #              raise UserError("Sold properties not be cancelled.")
    #         else:
    #             record.state="canceled"

    