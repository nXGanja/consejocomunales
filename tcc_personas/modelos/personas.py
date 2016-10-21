# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class tcc_personas(osv.osv):
	_name = 'tcc.personas'
	_inherits = {'res.users': 'user_id'}

	_columns={
		'consejocomunal_id': fields.many2one('res.partner','Consejo Comunal'),
		'familia_id': fields.many2one('tcc.familias','Nombre del Grupo Familiar'),
		'p_nombre': fields.char('Primer Nombre'),
		's_nombre': fields.char('Segundo Nombre'),
		'p_apellido': fields.char('Primer Apellido'),
		's_apellido': fields.char('Segundo Apellido'),
		'fecha_nacimiento': fields.date('Fecha de Nacimiento'),
		'nacionalidad': fields.selection([('Venezolano','Venezolano'),('Estranjero','Estranjero')],'Nacionalidad'),
		'cedula': fields.integer('Cedula'),
		'telefono': fields.char('Telefono'),
		'sexo': fields.selection([('masculino','Masculino'),('femenino','Femenino')],'Sexo'),
		'status': fields.selection([('vivo','Vivo'),('muerto','Muerto')],'Estado'),
		'active': fields.boolean('Activo',default=True),
	}