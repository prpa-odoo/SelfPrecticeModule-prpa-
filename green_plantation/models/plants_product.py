from odoo import fields,models,api

class PlantProduct(models.Model):
    _name="plant.product"
    _description="See All Available Products"
    _rec_name="contact_no"

    nursery_name=fields.Many2one('product.vendor',required=True)
    contact_no=fields.Char(compute='_compute_contactno')
    address=fields.Text(compute='_compute_address')
    email=fields.Char(compute='_compute_email')
    name=fields.Char(required=True,string="Product Title")
    description=fields.Text(required=True,string="Description")
    product_category=fields.Selection(
        string='Type',required=True,
        selection = [('plants','Plants'),('medicine','Medicine'),('tools','Tools')],
        )

    product_plant_id=fields.Many2one('product.category.plant',string="Plants")
    product_fertilizer_id=fields.Many2one('product.category.fertilizer',string="Fertilizer")
    product_seeds_id=fields.Many2one('product.category.seeds',string="Seeds")
    product_soil_id=fields.Many2one('product.category.soil',string="Soil")
    product_water_id=fields.Many2one('product.category.water',string="Water")
    product_plantproduct_id=fields.Many2one('product.category.plant.product',string="Plant Product")
    product_tools_id=fields.Many2one('plant.tools',string="Tools")
    product_medicine_id=fields.Many2one('plant.medicine',string="Medicine")
    product_price=fields.Float(string="Price")
    product_img=fields.Image()
    product_weather_ids=fields.Many2many('product.temperature',string="Weather Condition")

    quantity=fields.Integer()
    unit_price=fields.Integer()
    taxes=fields.Integer()
    sub_total=fields.Integer()
    order_type_id=fields.Many2one('order.orders',string="Orders")

    
    product_quantity=fields.Integer(string="Available Quantity")

    @api.depends('nursery_name.contact_no')
    def _compute_contactno(self):
        for record in self:
            record.contact_no=self.nursery_name.contact_no

    @api.depends('nursery_name.address')
    def _compute_address(self):
        for record in self:
            record.address=self.nursery_name.address

    @api.depends('nursery_name.email')
    def _compute_email(self):
        for record in self:
            record.email=self.nursery_name.email

    _sql_constraints = [
        ('check_price','CHECK(product_price > 0)','Price Must Be Greter Then 0.'),

    ]

   



