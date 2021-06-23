from pathlib import Path
import pandas as pd

personality_csv_file = Path.cwd().joinpath('personality-isf2018', 'personality-data.csv')

df = pd.read_csv (personality_csv_file,
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

#df = pd.read_csv(personality_csv_file)
movie_1_list = list(df['movie_1'])
print(movie_1_list)
#print(subdataframe)



# user_id  user_personality  movie_id_1_movielens   
# movie_id_1_tmdb  movie_title  movie_personality   movie_genres

# 