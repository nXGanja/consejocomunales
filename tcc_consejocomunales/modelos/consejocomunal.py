# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class consejocomunal(osv.osv):
	_name = 'tcc.consejocomunales'
	_inherits = {'res.partner': 'partner_id'}
	
	_columns={
		'rif': fields.char('RIF'),
		'codigo_situr': fields.char('Codigo Situr'),
		'fecha_constitucion': fields.date('Fecha de Constitución'),
		'estado_id': fields.many2one('tcc.estados','Estado',ondelete="restrict"),
		'municipio_id': fields.many2one('tcc.municipios','Municipio',ondelete="restrict"),
		'parroquia_id': fields.many2one('tcc.parroquias','Parroquia',ondelete="restrict"),
		'active': fields.boolean('Activo', default=True),
	}
	