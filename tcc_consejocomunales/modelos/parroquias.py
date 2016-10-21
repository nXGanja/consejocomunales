# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class parroquias(osv.osv):
	_name = 'tcc.parroquias'
	_rec_name = 'nombre'

	_columns={
		'nombre': fields.char('Nombre de la Parroquia'),
		'active': fields.boolean('Activo', default=True),
	}