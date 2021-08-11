from generating_temp_dataset import movielens_ids_of_final_db
from pathlib import Path
import pandas as pd


class Movie:
    #big_five is a dict
    def __init__(self, movielens_id, user_rating):

        movies_csv = Path.cwd().joinpath('movie_personality_and_genres.csv')

        movies_df = pd.read_csv(movies_csv,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movielensId',
                                 'imdbId',
                                 'extroversion',
                                 'neuroticism',
                                 'agreeableness',
                                 'conscientiousness',
                                 'openess',
                                 'Action',
                                 'Adventure',
                                 'Animation',
                                 'Comedy',
                                 'Crime',
                                 'Documentary',
                                 'Drama',
                                 'Family',
                                 'Fantasy',
                                 'History',
                                 'Horror',
                                 'Music',
                                 'Mystery',
                                 'Romance',
                                 'Science Fiction',
                                 'Thriller',
                                 'TV Movie',
                                 'War',
                                 'Western',
                                 'None'
                                ]                              
                        )
        

        movie_genres =  ['Action',
                        'Adventure',
                        'Animation',
                        'Comedy',
                        'Crime',
                        'Documentary',
                        'Drama',
                        'Family',
                        'Fantasy',
                        'History',
                        'Horror',
                        'Music',
                        'Mystery',
                        'Romance',
                        'Science Fiction',
                        'Thriller',
                        'TV Movie',
                        'War',
                        'Western',
                        'None']

        found_object = movies_df[movies_df['movielensId'] == movielens_id]

        self.genre = []

        if not found_object.empty:
        
            self.movielens_id = movielens_id
            self.imdb_id = found_object['imdbId'].item()
            self.extroversion = found_object['extroversion'].item()
            self.neuroticism = found_object['neuroticism'].item()
            self.agreeableness = found_object['agreeableness'].item()
            self.conscientiousness = found_object['conscientiousness'].item()
            self.openess = found_object['openess'].item()
            self.rating = user_rating
            

            for genre in movie_genres:
                self.genre.append(found_object[genre].item())

        else:
            self.movielens_id = "INVALID"


    def print_movie(self):

        if self.movielens_id == 'INVALID':
            print("non_existant movie!\n")
        else:
            print("movielensId: ", self.movielens_id)
            print("imdbId: ", self.imdb_id)
            print("extroversion: ", self.extroversion)
            print("neuroticism", self.neuroticism)
            print("agreeableness: ", self.agreeableness)
            print("conscientiousness: ", self.conscientiousness)
            print("openess: ", self.openess)
            print("user rating: ", self.rating)

            print("movie genres: \n")
            for genre in self.genre:
                print(genre)

if __name__ == '__main__':
    
    # filme existente:
    movie_test = Movie(115713, 4)
    movie_test.print_movie()
   


    # o filme abaixo não existe:
    movie_test = Movie(26674, 2)
    movie_test.print_movie()