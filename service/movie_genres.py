from models.movie_genres import MovieGenres as MovieGenresModel



class MovieGenresService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_genres(self) -> MovieGenresModel:
        result = self.db.query(MovieGenresModel).all()
        return result

    def create_movie_genres(self,movie_genres: MovieGenresModel):
        new_movie_genres = MovieGenresModel(
            mov_id = movie_genres.movie_id,
            gen_id = movie_genres.gen_id,

        )
        self.db.add(new_movie_genres)
        self.db.commit()
        return