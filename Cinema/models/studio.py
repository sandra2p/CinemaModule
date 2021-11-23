from odoo import api, models, fields
class CinemaStudio(models.Model):
    _name = "cinema.studio"#·importante tiene que empezar por minusculas 
    number= fields.Integer(string="Number of the studio")
    movie_ids= fields.Many2many('cinema.movie', 'cinema_studio_movie_rel', 'studio_id', 'movie_id', string="Movies")