# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class familias(osv.osv):
	_name = 'tcc.familias'
	_rec_name = 'nombre_familia'

	_columns={
		'consejocomunal_id': fields.many2one('res.partner','Consejo Comunal'),
		'nombre_familia': fields.char('Nombre del Grupo Familiar'),
		'fecha_residente': fields.date('Desde cuando Reside'),
		'casa_id': fields.many2one('tcc.casas', 'Casa'),
		'edificio_id': fields.many2one('tcc.edificios','Edificio'),
		'piso_id': fields.many2one('tcc.pisos','Piso'),
		'apartamento_id': fields.many2one('tcc.apartamentos','Apartamento'),
		'tipo_vivienda': fields.selection([('casa','Casa'),('edificio','Edificio')],'Tipo de Vivienda'),
		'tenencia': fields.selection([('propia','Propia'),('alquilada','Alquilada'), ('invadida','Invadida'), ('arrimado','arrimado')],'Tenencia'),
		'active': fields.boolean('Activo',default=True),
	}

	