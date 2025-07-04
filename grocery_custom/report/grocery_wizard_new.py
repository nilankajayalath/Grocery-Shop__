from odoo import models

class ParticularReport(models.AbstractModel):
    _name = 'report.grocery_custom.report_grocery_new'

    def _get_report_values(self, docids, data=None):
        
        obj = self.env['grocery.details'].search([('expiry_date', '>=', data['start_date']),
                                                  ('expiry_date', '<=', data['end_date'])])
        sale_orders = self.env['sale.order'].search([])
        print(sale_orders)
        # return a custom rendering context
        return {
            'docs': obj,
            'my_sales_order': sale_orders
        }   