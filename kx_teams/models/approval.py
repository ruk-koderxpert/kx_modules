from odoo import fields, models, _

class Approvals(models.Model):
    _name = "approvals.approvals"

    approver_id = fields.Many2one('team.team')
    action_date = fields.Datetime('Time')
    active = fields.Boolean(string="Active", default=True)
    is_approved = fields.Boolean()
    is_rejected = fields.Boolean()
    rejection_reason = fields.Text()
    sequence = fields.Integer()
    user_id = fields.Many2one('res.users', string="User")

    def unlink(self):
        teams = self.mapped('approver_id')
        res = super().unlink()
        teams._reorder_sequence()
        return res
