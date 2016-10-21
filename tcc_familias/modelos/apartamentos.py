# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class apartamentos(osv.osv):
	_name = 'tcc.apartamentos'

	_columns={
		'numero': fields.char('Numero'),
		'active': fields.boolean('Activo',default=True),
	}