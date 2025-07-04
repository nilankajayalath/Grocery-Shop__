# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Grocery Shop Custom',
    'version' : '17.0.0.1',
    'summary': 'Grocery Details Management System',
    'sequence': 1,
    'description': """
Grocery Details
====================
Thjshxghjdghcdbhfjhj jhvjgeuhebehgrn erfjnvbkjkedf case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Others',
    'website': 'https://www.ocore48.com',
    'depends': ['grocery_shop','sale_management'],
    'data': [
             'security/security.xml',   
             'security/ir.model.access.csv',
             'data/paper_format_report.xml',  
             'security/record_rule.xml',
             'view/grocery_details_view.xml',
             'view/menu_overide.xml',
             'report/report_grocery_new.xml',
             'report/ir_actions_report.xml',
             'report/report_grocery_templates.xml', 
             'wizard/grocery_wizard_views.xml',
             'wizard/grocery_report_wizard_views.xml',
            
             
                 
          ],
   
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}