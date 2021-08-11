from generating_temp_dataset import movielens_ids_of_final_db
from pathlib import Path
import pandas as pd


class Movie:
    #big_five is a dict
    def __init__(self, movielens_id):

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
        
        found_object = movies_df[movies_df['movielensId'] == movielens_id]
        print(found_object)
        '''
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_rating = movie_rating
        self.movie_script = movie_script
        self.extroversion = big_five['extroversion']
        self.neuroticism = big_five['neuroticism']
        self.agreeableness = big_five['agreeableness']
        self.conscientiousness = big_five['conscientiousness']
        self.openess = big_five['openess']
        self.genre = genre
        '''

if __name__ == '__main__':
    movie_test = Movie(115713)