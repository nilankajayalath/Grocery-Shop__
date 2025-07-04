from odoo import models, fields

class GroceryReportWizard(models.TransientModel):
    _name = 'grocery.report.wizard'
    _description = 'Grocery Report Wizard'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    def action_generate_report(self):
        self.ensure_one()

        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

        return self.env.ref('grocery_custom.action_report_grocery_details_wizard').report_action([], data=data)
