#maps the movielens id with title
from pathlib import Path
import pandas as pd

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

# 58098 movies
#print(len(df))

find = 24
#print(df['movieId'][find])

found_object = df[df["movieId"] == find]
# estudar pandas series pra poder 
# converter o titulo numa string:
print(found_object['title'])



#def map_movielens_id_and_title(movielens_id):


