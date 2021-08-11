from generating_temp_dataset import create_genre_columns
from pathlib import Path
import pandas as pd
import UserItem as UI

def create_UserItem_teste():

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

    i = 0
    users = []
    for index, row in personality_data_df.iterrows():
        #print (row)

        user_movies = []

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

        for movie in movie_items:
            user_movies.append(row[movie])

        big_five = {}
        big_five['extraversion'] = row['extraversion']
        big_five['emotional_stability'] = row['emotional_stability']
        big_five['agreeableness'] = row['agreeableness']
        big_five['conscientiousness'] = row['conscientiousness']
        big_five['openess'] = row['openness']


        user = UI.UserItem(row['userid'], user_movies, big_five)

        users.append(user)
        i+=1
        if i == 1:
            break
    
    for new_user in users:
        new_user.print_user()
    #print(personality_data_df)
#personality_csv_file = Path.cwd().joinpath('personality-isf2018', 'personality-data.csv')
#movie_dat_file = Path.cwd().joinpath('tag-genome', 'movies.dat')

if __name__ == '__main__':

    create_UserItem_teste()