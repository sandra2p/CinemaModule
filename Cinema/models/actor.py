from odoo import api, models, fields
class CinemaActor(models.Model):
    _inherit="cinema.person"
    _name = "cinema.actor"
    #name= fields.Char(string="Name")
    #age = fields.Float('Age', digits=(12, 1))
    movie_id= fields.Many2one('cinema.movie', string="Pelicula")
    ganancias_peliculas=fields.Integer(string="$/movies")
    ganancias_publi=fields.Integer(string="$/publi")
    ganancias_interviews=fields.Integer(string="$/interviews") 
    media_ganancias=fields.Float(string="ganacias medias por año", compute='_get_average') 

    @api.depends('ganancias_peliculas', 'ganancias_publi', 'ganancias_interviews')
    def _get_average(self):
        for record in self:
            record.media_ganancias = (record.ganancias_interviews + record.ganancias_publi + record.ganancias_peliculas ) / 3   
    
