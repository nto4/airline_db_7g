# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class airline_db_7g(models.Model):
#     _name = 'airline_db_7g.airline_db_7g'
#     _description = 'airline_db_7g.airline_db_7g'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
