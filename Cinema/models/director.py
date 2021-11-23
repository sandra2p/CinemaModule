from odoo import api, models, fields
class CinemaDirector(models.Model):
    _name = "cinema.director"#·importante tiene que empezar por minusculas 
    name= fields.Char(string="Name")
    age = fields.Float('Age', digits=(12, 1))