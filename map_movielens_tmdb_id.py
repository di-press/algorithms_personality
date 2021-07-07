#maps the movielens id with tmdb id
from movielens_id_title import find_title_by_movielens_id
from os import name
from pathlib import Path
import pandas as pd

def create_link_df():

    movie_csv_file = Path.cwd().joinpath('movielens','ml-latest', 'links.csv')

    df = pd.read_csv (movie_csv_file,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movieId',
                                   'imdbId',
                                   'tmdbId']
                    )

    # returns a deep copy; the original df won't never be modified
    # df contains 58098 movies
    return df.copy(deep=True)

def find_tmdb_id(movielens_ids, link_df):
    
    id_title_tuples = []

    for id in movielens_ids:
        print("buscando id: ", id)
        #id = int(id)
        find = id
        #print(df['movieId'][find])

        found_object = link_df[link_df["movieId"] == find]

        # if the search in the dataframe didn't return a value:
        if not found_object.empty:
        
            movie_imdb_id = found_object['imdbId'].item()
            movie_imdb_id = str(movie_imdb_id)
            
            if(len(movie_imdb_id) < 7):

                complementary_zeros = 7 - len(movie_imdb_id)

                fill_zeros = ''

                for _ in range(complementary_zeros):
                    fill_zeros += '0'

                movie_imdb_id = fill_zeros + movie_imdb_id

            movie_imdb_id = 'tt' + movie_imdb_id
            # id is a number
            id_title_tuples.append((id, movie_imdb_id))

            #print(movie_title)
    
    return id_title_tuples


if __name__ == '__main__':

    link_df = create_link_df()
    #print(df)
    movielens_ids = [122900, 1, 149300]
    found_objects = find_tmdb_id(movielens_ids, link_df)
    print(found_objects)