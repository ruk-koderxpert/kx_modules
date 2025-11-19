from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    approval = fields.Boolean(string="Sales Order Approval")
    approval_validation_amount = fields.Monetary(string="Minimum Amount for Double Validation", default=5000)
