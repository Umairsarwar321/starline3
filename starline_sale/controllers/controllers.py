# -*- coding: utf-8 -*-
# from odoo import http


# class StarlineSale(http.Controller):
#     @http.route('/starline_sale/starline_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/starline_sale/starline_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('starline_sale.listing', {
#             'root': '/starline_sale/starline_sale',
#             'objects': http.request.env['starline_sale.starline_sale'].search([]),
#         })

#     @http.route('/starline_sale/starline_sale/objects/<model("starline_sale.starline_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('starline_sale.object', {
#             'object': obj
#         })
