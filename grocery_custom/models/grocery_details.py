from odoo import models, fields, api

class GroceryDetails(models.Model):
    _inherit = 'grocery.details'
  
    brand_name = fields.Char(string="Brand Name")  
    quantity = fields.Integer(string='New Quantity')
    contact_ids = fields.One2many('grocery.contact', 'grocery_id', string='Contacts')
    edit_id= fields.Integer(string='Edit ID')
    edit_value= fields.Char(string='Edit Value')

  

    def inherited_grocery_store(self):
        for rec in self:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Info',
                    'message': f'Item "{rec.name}" has {rec.quantity} in stock.',
                    'sticky': False,
                }
            }
        
    def check_availability(self):
        for rec in self:
            availability = 'available' if rec.in_stock else 'not available'
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Availability',
                    'message': f'Item "{rec.name}" is {availability}.',
                    'sticky': False,
                }
            }     
        
          # add button thods (these are placeholders; customize as needed)
    def add_contact(self):
        for rec in self:
            rec.contact_ids = [(0,0, {
                'name': 'New Contact',
                'phone': '1234567890',
                'email': 'test@test.com' 
            })]

    def edit_contact(self):
        self.contact_ids = [(1, self.edit_id, {
            'email': self.edit_value,
            'name': self.edit_value,
            'phone': self.edit_value
        })]
            

    def clear_contact(self):
        for rec in self:
            rec.contact_ids.unlink()  # Clears all contacts linked to this grocery
        

        


        
    # @api.model
    # def create(self, values):
    #     print(values)
    #     result = super(GroceryDetails,self).create(values)
        
    #     return result
    
    # def write(self, values):
    #     grocery = self.env['grocery.details'].search([('id', '=', self.id)])
    #     print(grocery.name,'--------',self.name)
    #     result = super(GroceryDetails,self).write(values)
    #     groery = self.env['grocery.details'].search([('id', '=', self.id)])
    #     print(groery.name,'--------',self.name)
    #     return result
    
    # def unlink(self):
        
    #     result = super(GroceryDetails, self).unlink()
        
    #     return result
    
    # def action_mark_as_category(self):
    #     result = super(GroceryDetails,self).action_mark_as_category()
    #     print('aaaa')
    #     return result