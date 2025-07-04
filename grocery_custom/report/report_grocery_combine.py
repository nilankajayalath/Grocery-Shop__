from odoo import models

class ParticularReport(models.AbstractModel):
    _name = 'report.grocery_custom.report_grocery_new'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('grocery_custom.report_grocery_new')
        # get the records selected for this rendering of the report
        obj = self.env[report.model].browse(docids)
      
        
        sale_orders = self.env['sale.order'].search([])
        print(sale_orders)
        # return a custom rendering context
        return {
            'docs': obj,
            'my_sales_order': sale_orders
        }