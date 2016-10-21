# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class estados(osv.osv):
	_name = 'tcc.estados'
	_rec_name = 'nombre'

	_columns={
		'nombre': fields.char('Nombre del Estado'),
		'active': fields.boolean('Activo', default=True),
	}
	