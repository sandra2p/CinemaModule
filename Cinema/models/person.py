from odoo import api, models, fields
class CinemaPerson(models.Model):
    _name = "cinema.person"#·importante tiene que empezar por minusculas 
    name= fields.Char(string="Name")
    age = fields.Float('Age', digits=(12, 1))