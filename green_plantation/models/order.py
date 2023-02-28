from odoo import fields,models,api

class Order(models.Model):
    _name="order.orders"
    _description="See All Orders"
    # _inherit = "res.users"

    product_name=fields.Many2one('plant.product',required=True,string="Product Name")
    description=fields.Text(related="product_name.description",string="description")
    quantity=fields.Integer()
    unit_price=fields.Integer()
    sub_total=fields.Integer(compute="_compute_price")
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

    @api.depends('unit_price','quantity')
    def _compute_price(self):
        for record in self:
                record.sub_total = record.quantity * record.unit_price
