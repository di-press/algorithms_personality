#maps the movielens id with title
from os import name
from pathlib import Path
import pandas as pd

def create_df():

    movie_csv_file = Path.cwd().joinpath('movielens','ml-latest', 'movies.csv')

    df = pd.read_csv (movie_csv_file,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movieId',
                                    'title',
                                    'genres'] 

                    )

    # returns a deep copy; the original df won't never be modified
    # df contains 58098 movies
    return df.copy(deep=True)


def find_title_by_movielens_id(movielens_id, df):

    find = movielens_id
    #print(df['movieId'][find])

    found_object = df[df["movieId"] == find]
    movie_title = found_object['title'].item()


    print(movie_title)

def find_titles(movielens_ids):

    movie_csv_file = Path.cwd().joinpath('movielens','ml-latest', 'movies.csv')

    df = pd.read_csv (movie_csv_file,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movieId',
                                    'title',
                                    'genres'] 

                    )

    for id in movielens_ids:
        
        find = id
        found_object = df[df["movieId"] == find]
        movie_title = found_object['title'].item()


        print(movie_title)

if __name__ == "__main__":

    movielens_ids = [24]
    
    find_titles(movielens_ids)
