from pathlib import Path
import pandas as pd
import movielens_id_title

personality_csv_file = Path.cwd().joinpath('personality-isf2018', 'personality-data.csv')

personality_data_df = pd.read_csv (personality_csv_file,
                    sep=", ", warn_bad_lines=True, 
                    error_bad_lines=True,
                    engine='python',
                    header=0,
                    usecols = ['userid', 
                               'openness', 
                               'agreeableness', 
                               'emotional_stability',
                               'conscientiousness', 
                               'extraversion',
                               'assigned metric', 
                               'assigned condition', 
                               'movie_1', 
                               'predicted_rating_1',
                               'movie_2', 
                               'predicted_rating_2', 
                               'movie_3', 
                               'predicted_rating_3', 
                               'movie_4', 
                               'predicted_rating_4', 
                               'movie_5', 
                               'predicted_rating_5', 
                               'movie_6', 
                               'predicted_rating_6', 
                               'movie_7', 
                               'predicted_rating_7', 
                               'movie_8', 
                               'predicted_rating_8', 
                               'movie_9', 
                               'predicted_rating_9', 
                               'movie_10', 
                               'predicted_rating_10', 
                               'movie_11', 
                               'predicted_rating_11', 
                               'movie_12', 
                               'predicted_rating_12', 
                               'is_personalized', 
                               'enjoy_watching'] 

                )

#personality_data_df = pd.read_csv(personality_csv_file)

movie_items =  ['movie_1',
                'movie_2',
                'movie_3',
                'movie_4',
                'movie_5',
                'movie_6',
                'movie_7',
                'movie_8',
                'movie_9',
                'movie_10',
                'movie_11',
                'movie_12']

all_movies = []

for item in movie_items:

    all_movies += list(personality_data_df[item])


# all_movies contains 2415 different movies
all_movies = set(all_movies)


movielens_data_df = movielens_id_title.create_df()

movielens_id_title.find_title_by_movielens_id(all_movies, movielens_data_df)






# user_id  user_personality  movie_id_1_movielens   
# movie_id_1_tmdb  movie_title  movie_personality   movie_genres

# 