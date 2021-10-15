# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
#from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Cursos'
     #_name = 'open_academy.open_academy'
     #_description = 'Cursos'

    name = fields.Char(string='Title' ,required=True)
     #value = fields.Integer()
     #value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

     #@api.depends('value')
     #def _value_pc(self):
         #for record in self:
             #record.value2 = float(record.value) / 100


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")