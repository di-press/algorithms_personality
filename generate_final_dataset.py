from generating_temp_dataset import create_genre_columns, movielens_ids_of_final_db
from pathlib import Path
import pandas as pd
import UserItem as UI
import Movie

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

    user_and_movies_objects = []
    i = 0
    users = []
    for index, row in personality_data_df.iterrows():
        #print ("row é: ", row)

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

        #print("user_movies :", user_movies)
        big_five = {}
        big_five['extraversion'] = row['extraversion']
        big_five['emotional_stability'] = row['emotional_stability']
        big_five['agreeableness'] = row['agreeableness']
        big_five['conscientiousness'] = row['conscientiousness']
        big_five['openess'] = row['openness']

        user = UI.UserItem(row['userid'], user_movies, big_five)

        users.append(user)
        #print("users é: ", users)

        movie_ratings = []
        labels_ratings = ['predicted_rating_1',
                            'predicted_rating_2',                                 
                            'predicted_rating_3',  
                            'predicted_rating_4', 
                            'predicted_rating_5', 
                            'predicted_rating_6', 
                            'predicted_rating_7', 
                            'predicted_rating_8', 
                            'predicted_rating_9', 
                            'predicted_rating_10', 
                            'predicted_rating_11', 
                            'predicted_rating_12'
                        ]

        for label in labels_ratings:
            movie_ratings.append(row[label])

        #print("movie_rating é: ", movie_ratings)

        movie_and_rating = list(zip(user_movies, movie_ratings))
        #print("movie and rating: ",movie_and_rating)

        movies_objects = []

        for items in movie_and_rating:

            new_movie = Movie.Movie(items[0], items[1])
            #print("new_movie é: \n", new_movie)
            #Movie.print_movie(new_movie)
            #new_movie.print_movie()
            
            if new_movie.movielens_id != 'INVALID':
                movies_objects.append(new_movie)
                #print("movielens Id desse filme é: ", new_movie.movielens_id)
            
        user_and_movies_objects.append((user, movies_objects))

        i+=1
        if i == 1:
            break
    
    return user_and_movies_objects

   
def create_final_dataset_test(movie_user_list):

    df_row_tuples = []

    for objects in movie_user_list:
        user = objects[0]
        movie_list = objects[1]

        for movie in movie_list:
            row_tuple = (user, movie)
            df_row_tuples.append(row_tuple)

    for item in df_row_tuples:
        print("linha: \n")
        item[0].print_user()
        item[1].print_movie()


if __name__ == '__main__':

    movie_user_list = create_UserItem_teste()
    #print("movie_user_list é: ", movie_user_list)
    create_final_dataset_test(movie_user_list)