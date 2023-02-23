from odoo import fields,models,api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class PlantOffers(models.Model):
    _name="plant.offer"
    _description="Plant Offer"

    price = fields.Float()
    partner_id=fields.Many2one('res.partner',required=True)
    validity=fields.Integer(default=7)
    date_deadline=fields.Date(compute='_compute_date',inverse='_inverse_date',readonly=False)

    status = fields.Selection(
        string='Status',
        selection = [('accept','Accepted'),('refused','Refused')],
        copy=False
     )

    offer_id=fields.Many2one('plant.product',string="Offers")

    @api.depends('create_date','validity')
    def _compute_date(self):
        for record in self:
            if record.create_date:
                date = record.create_date.date()
                record.date_deadline = date + relativedelta(days=record.validity)
            else:
                date=datetime.today()
                record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            if record.date_deadline > datetime.date(datetime.today()):
                record.validity = (record.date_deadline - record.create_date.date()).days
            else:
                record.validity=0


    def action_accept(self):
        for record in self:
            record.status="accept"

    def action_cancle(self):
        for record in self:
            record.status="refused"