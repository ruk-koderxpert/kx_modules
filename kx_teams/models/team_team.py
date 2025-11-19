from odoo import api, fields, models

class Team(models.Model):
    _name = "team.team"
    _description = "Approval Team"

    def _default_model_ids(self):
        default_models = [
            'purchase.model_purchase_order',
            'sale.model_sale_order',
            'account.model_account_move',
        ]
        model_ids = [
            self.env.ref(model_ref, raise_if_not_found=False).id
            for model_ref in default_models
            if self.env.ref(model_ref, raise_if_not_found=False)
        ]
        return [(6, 0, model_ids)] if model_ids else []

    active = fields.Boolean(string="Active", default=True)
    approval = fields.Boolean(string="Based on Amount", related='company_ids.approval', readonly=False)
    approval_validation_amount = fields.Monetary(string="Minimum Amount", related='company_ids.approval_validation_amount', currency_field='company_currency_id', readonly=False)
    approvers_ids = fields.One2many('approvals.approvals', 'approver_id', string="Approvers")
    company_currency_id = fields.Many2one('res.currency', related='company_ids.currency_id', string="Company Currency", readonly=True)
    company_ids = fields.Many2many('res.company', default=lambda self: self.env.company.ids)
    model_ids = fields.Many2many('ir.model', string='Models', default=_default_model_ids)
    member_ids = fields.Many2many('res.users', string="Team Members")
    name = fields.Char(string="Team Name", required=True)
    sequence = fields.Integer(string='Sequence')
    user_id = fields.Many2one('res.users', string="Team Leader", required=True)

    def _reorder_sequence(self):
        """Reorder approvers' sequence starting from 0 within each team."""
        for team in self:
            approvers = team.approvers_ids.sorted(key=lambda r: r.sequence or 0)
            for idx, approver in enumerate(approvers):
                approver.sequence = idx

    @api.onchange('user_id')
    def _onchange_user_id(self):
        """Ensure the selected team leader is always included in the members list."""
        if self.user_id:
            member_ids = set(self.member_ids.ids)
            member_ids.add(self.user_id.id)
            self.member_ids = [(6, 0, list(member_ids))]
