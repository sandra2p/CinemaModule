from odoo import api, models, fields
class CinemaActor(models.Model):
    _inherit="cinema.person"
    _name = "cinema.actor"
    #name= fields.Char(string="Name")
    #age = fields.Float('Age', digits=(12, 1))
    movie_id= fields.Many2one('cinema.movie', string="Pelicula")

    