from odoo import fields,models,api
from datetime import datetime

class Order(models.Model):
    _name="order.orders"
    _description="See All Orders"
    # _inherit = "res.users"
    # _inherit = ""
    _rec_name="seq_name"

    quantity=fields.Integer()
    unit_price=fields.Integer()
    

    user_id=fields.Many2one('res.partner',string="Customer")
    address=fields.Char(related='user_id.contact_address',string="Address")
    email=fields.Char(related='user_id.email',string="Email")

    date = fields.Datetime(string="Creation Date",readonly=True, default=lambda self:(fields.Datetime.now()))


    product_ids=fields.Many2many("plant.product",string="product")
    order_ids = fields.One2many("plant.product", "order_type_id")

    seq_name = fields.Char(string='Order Sequence', required=True,readonly=True, default=lambda self: ('New'))
    product_category=fields.Selection(
        string='Type',tracking=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )
    total = fields.Float()


    # def action_cancle(self):
    #     for record in self:
    #         if record.state == "sold":
    #              raise UserError("Sold properties not be cancelled.")
    #         else:
    #             record.state="canceled"

    
    #sequence 
    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('order.orders')
        return super(Order,self).create(vals)

    # @api.depends('sub_total')
    # def _compute_total(self):
    #     for record in self:
    #         record.total = self *record.product_ids.sub_total

    