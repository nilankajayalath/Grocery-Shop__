from odoo import models, fields, api

class GroceryContact(models.Model):
    _name = 'grocery.contact'
    _description = 'Grocery Contact Details'

    name = fields.Char(string='Contact Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    grocery_id = fields.Many2one('grocery.details', string='Grocery Item', ondelete='cascade')

