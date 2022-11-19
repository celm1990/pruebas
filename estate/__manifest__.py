# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Estate',
    'version' : '12.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 15,
    'description': """
    """,
    'category': 'Invoicing Management',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base', 'product'],
    'data': [
        "security/estate_security.xml",
        "security/ir.model.access.csv",
        "views/pacientes_view.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
