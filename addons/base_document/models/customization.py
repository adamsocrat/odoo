from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    billing_period_start = fields.Datetime(string='BillingPeriodStart')
    billing_period_end = fields.Datetime(string='BillingPeriodEnd')
