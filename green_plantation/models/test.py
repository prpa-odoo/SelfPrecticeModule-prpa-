from odoo import fields,models,api

class PlantProductTest(models.Model):
    _inherit = "plant.product"
    _description="See All Available Products"



    def action_instock(self):
        for record in self:
            if self.product_category == "plants":
                self.env['product.category.plant'].create({
                    "name" : self.name
                })

            if self.product_category == "medicine":
                self.env['plant.medicine'].create({
                    "name" : self.name
                })

            if self.product_category == "tools":
                self.env['plant.tools'].create({
                    "name" : self.name
                })
                
                return super(PlantProductTest,self).action_instock()
            
