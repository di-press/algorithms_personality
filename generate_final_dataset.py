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
        if i == 5:
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

def create_UserItem():

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

    
    return user_and_movies_objects

   

def create_final_dataset(movie_user_list):

    df_row_tuples = []

    for objects in movie_user_list:
        user = objects[0]
        movie_list = objects[1]

        for movie in movie_list:
            row_tuple = (user, movie)
            df_row_tuples.append(row_tuple)

    '''
    user_ids = []
    user_extroversion = []
    user_neuroticism = []
    user_agreeableness = []
    user_conscientiousness = []
    user_openess = []
    watched_movie_movielens_Id = []
    watched_movie_imdb_Id = []
    movie_extroversion = []
    movie_neuroticism = []
    movie_agreeableness = []
    movie_conscientiousness = []
    movie_openess = []
    action = []
    adventure = []
    animation = []
    comedy = []
    crime = []
    documentary = []
    drama = []
    family = []
    fantasy = []
    history = []
    horror = []
    music = []
    mystery = []
    romance = []
    science_fiction = []
    thriller = []
    tv_movie = []
    war = []
    western = []
    none = []
    movie_rating = []
    '''

    df_rows = []

    for item in df_row_tuples:
        
        current_user = item[0]
        current_movie = item[1]

        current_neuroticism = 7 - current_user.emotional_stability

        user_item_tuple = (current_user.hash_id,
                           current_user.extraversion,
                           #neuroticism is the opposite of emotional stability:
                            current_neuroticism,
                            current_user.agreeableness,
                            current_user.conscientiousness,
                            current_user.openess,
                            current_movie.movielens_id,
                            current_movie.imdb_id,
                            current_movie.extroversion,
                            current_movie.neuroticism,
                            current_movie.agreeableness,
                            current_movie.conscientiousness,
                            current_movie.openess,
                            current_movie.genre[0],
                            current_movie.genre[1],
                            current_movie.genre[2],
                            current_movie.genre[3],
                            current_movie.genre[4],
                            current_movie.genre[5],
                            current_movie.genre[6],
                            current_movie.genre[7],
                            current_movie.genre[8],
                            current_movie.genre[9],
                            current_movie.genre[10],
                            current_movie.genre[11],
                            current_movie.genre[12],
                            current_movie.genre[13],
                            current_movie.genre[14],
                            current_movie.genre[15],
                            current_movie.genre[16],
                            current_movie.genre[17],
                            current_movie.genre[18],
                            current_movie.genre[19],
                            current_movie.rating
                        )

        df_rows.append(user_item_tuple)

    final_dataset_df = pd.DataFrame(df_rows,
                        columns = ['user_id',
                        'user_extroversion',
                        'user_neuroticism',
                        'user_agreeableness',
                        'user_conscientiousness',
                        'user_openess',
                        'movielens_Id',
                        'imdb_Id',
                        'movie_extroversion',
                        'movie_neuroticism',
                        'movie_agreeableness',
                        'movie_conscientiousness',
                        'movie_openess',
                        'action',
                        'adventure',
                        'animation',
                        'comedy',
                        'crime',
                        'documentary',
                        'drama',
                        'family',
                        'fantasy',
                        'history',
                        'horror',
                        'music',
                        'mystery',
                        'romance',
                        'science_fiction',
                        'thriller',
                        'tv_movie',
                        'war',
                        'western',
                        'none',
                        'movie_rating']                                       
                                )

    # data containing the plots and its personality:
    path_temp_csv = Path.cwd().joinpath('final_dataset.csv')
    # index = True star indexing the csv file with 0:
    final_dataset_df.to_csv(path_temp_csv, index = True)

if __name__ == '__main__':

    #movie_user_list = create_UserItem_teste()
    #print("movie_user_list é: ", movie_user_list)
    #create_final_dataset_test(movie_user_list)

    movie_user_list = create_UserItem()
    #print("movie_user_list é: ", movie_user_list)
    create_final_dataset(movie_user_list)