from odoo import models, fields, api

class DemoWizard(models.TransientModel):
    _name = 'demo.wizard'
    _description = 'Demo Wizard'

    task_ids_text = fields.Char(string="Selection Info")

    def action_confirm(self):
        return {'type':'ir.actions.act_window_close'}

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)


        active_ids = self.env.context.get('active_ids', [])
        res['task_ids_text'] = f"You selected {len(active_ids)} tasks."

        return res