from odoo import fields,models,api

class Order(models.Model):
    _name="order.orders"
    _description="See All Orders"
    # _inherit = "res.users"
    # _inherit = ""

    quantity=fields.Integer()
    unit_price=fields.Integer()
    sub_total=fields.Float(compute="_compute_price")

    product_ids=fields.Many2many("plant.product",string="product")
    order_ids = fields.One2many("plant.product", "order_type_id")

    seq_name = fields.Char(string='Order Sequence', required=True,readonly=True, default=lambda self: ('New'))
    product_category=fields.Selection(
        string='Type',required=True,tracking=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )
    total = fields.Float()

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

    #sequence 
    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('order.orders')
        return super(Order,self).create(vals)
