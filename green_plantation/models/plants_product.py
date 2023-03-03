from odoo import fields,models,api

class PlantProduct(models.Model):
    _name="plant.product"
    _description="See All Available Products"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name="name"
    # _inherit = "plant.product"

    nursery_name=fields.Many2one('product.vendor',required=True,store=True)
    contact_no=fields.Char(related='nursery_name.contact_no')
    address=fields.Text(related = 'nursery_name.address')
    email=fields.Char(related='nursery_name.email')
    name=fields.Char(required=True,string="Product Title")
    description=fields.Text(required=True,string="Description")
    product_category=fields.Selection(
        string='Type',required=True,tracking=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )
    sub_total=fields.Float()
    quantity=fields.Integer()
    unit_price=fields.Integer()

    product_plant_id=fields.Many2one('product.category.plant',string="Plants")

    plant_type_id = fields.Many2one(related = "product_plant_id", store = True)


    product_fertilizer_id=fields.Many2one('product.category.fertilizer',string="Fertilizer")
    product_seeds_id=fields.Many2one('product.category.seeds',string="Seeds")
    product_soil_id=fields.Many2one('product.category.soil',string="Soil")
    product_water_id=fields.Many2one('product.category.water',string="Water")
    product_plantproduct_id=fields.Many2one('product.category.plant.product',string="Plant Product")
    product_tools_id=fields.Many2one('plant.tools',string="Tools")
    tools_type_id = fields.Many2one(related='product_tools_id',store = True)


    product_medicine_id=fields.Many2one('plant.medicine',string="Medicine")
    medicine_type_id = fields.Many2one(related='product_medicine_id',store = True)

    product_img=fields.Image()
    product_weather_ids=fields.Many2many('product.temperature',string="Weather Condition")
    
    selling_price=fields.Float()
    best_price = fields.Float(compute="_compute_bestprice")

    order_type_id=fields.Many2one('order.orders',string="Orders")

    offer_ids=fields.One2many('plant.offer','offer_id',string="Available Offer")
    offer_status = fields.Selection(related="offer_ids.status")

    customer_id=fields.Many2one('res.partner',copy=False,string="Customer")
    owner_id=fields.Many2one('res.users',default=lambda self:self.env.user,string="owner")
    
    product_quantity=fields.Integer(string="Available Quantity")

    state = fields.Selection(
        string='State',
        selection = [('instock','In Stock'),('outstock','Out Of stock')],
        copy=False,tracking=True
    )

    # @api.depends('nursery_name.contact_no')
    # def _compute_contactno(self):
    #     for record in self:
    #         record.contact_no=self.nursery_name.contact_no

    # @api.depends('nursery_name.address')
    # def _compute_address(self):
    #     for record in self:
    #         record.address=self.nursery_name.address

    # @api.depends('nursery_name.email')
    # def _compute_email(self):
    #     for record in self:
    #         record.email=self.nursery_name.email

    def action_instock(self):
        for record in self:
            record.state="instock"
            

    def action_outstock(self):
        for record in self:
            record.state="outstock"

    @api.depends('offer_ids')
    def _compute_bestprice(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price=0.0

    


         

    

   



