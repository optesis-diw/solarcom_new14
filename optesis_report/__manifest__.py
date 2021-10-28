{
    'name': 'Solarcom Report',

    'description': """
                
            """,

    'author': 'OPTESIS SA BY ANG',
    'website': "http://www.Optesis.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '12.0.0.0.0',
    'category': 'Accounting',

    # any module necessary for this one to work correctly
    'depends': ['sale','base'],

    'data': [
        #'security/ir.model.access.csv',
        #'views/optesis_classe.xml',
        #'views/optesis_annee.xml',
        'views/solarcom_header_footer.xml',
        'views/solarcom_external_layout.xml',
        'views/solarcom_sale_order.xml',
        'views/solarcom_account_move.xml',
        'views/solarcom_purchase_order.xml',
        'views/solarcom_demande_prix.xml',
        'views/solarcom_stock_picking.xml',

        'report/custom_format.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],

}