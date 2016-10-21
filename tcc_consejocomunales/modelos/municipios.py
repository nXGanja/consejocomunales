# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class municipios(osv.osv):
	_name = 'tcc.municipios'
	_rec_name = 'nombre'

	_columns={
		'nombre': fields.char('Nombre del Municipio'),
		'active': fields.boolean('Activo', default=True),
	}