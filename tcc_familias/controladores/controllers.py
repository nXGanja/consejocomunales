# -*- coding: utf-8 -*-
from openerp import http

# class TccFamilias(http.Controller):
#     @http.route('/tcc_familias/tcc_familias/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tcc_familias/tcc_familias/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tcc_familias.listing', {
#             'root': '/tcc_familias/tcc_familias',
#             'objects': http.request.env['tcc_familias.tcc_familias'].search([]),
#         })

#     @http.route('/tcc_familias/tcc_familias/objects/<model("tcc_familias.tcc_familias"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tcc_familias.object', {
#             'object': obj
#         })