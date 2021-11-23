from odoo import api, models, fields
class CinemaMovie(models.Model):
    _name = 'cinema.movie'
    title= fields.Char(string="title")
    premiereDate= fields.Date(string="PremiereDate",
                             store=True,
                             default=fields.Date.today)
    year = fields.Integer(string="publication year")
    description = fields.Char(string="description")
    actor_ids= fields.One2many('cinema.actor', 'movie_id' ,string="cast")
    genres= especialidad = fields.Selection([
        ('ac', 'Action'),
        ('th', 'Thriller'),
        ('msc', 'Musical'),
        ('hr', 'Horror'),

    ], default='ac')
    studios_ids= fields.Many2many('cinema.studio', 'cinema_studio_movie_rel', 'movie_id', 'studio_id', string="Recording Studios")
    _sql_constraints = [('title', 'UNIQUE (title)',
                         'ya existe esa peli')]

