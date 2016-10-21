# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class pisos(osv.osv):
	_name = 'tcc.pisos'

	_columns={
		'numero': fields.integer('Numero'),
		'active': fields.boolean('Activo',default=True),
	}