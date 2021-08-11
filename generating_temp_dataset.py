from pathlib import Path
import pandas as pd
import map_movielens_imdb_id 
import tmdb_query as TmdbQuery
 

def movielens_ids_of_final_db():

    plot_personality_csv = Path.cwd().joinpath('plots_personalities.csv')

    plot_personality_df = pd.read_csv(plot_personality_csv,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movielensId',
                                 'extroversion',
                                 'neuroticism',
                                 'agreeableness',
                                 'conscientiousness',
                                 'openess']
                                
                        )

    movielens_ids = list(plot_personality_df['movielensId'])

    imdbs_ids = id_mapping(movielens_ids)
    
    column_values = pd.Series(imdbs_ids)
    plot_personality_df.insert(loc=1, column='imdbId', value=column_values)

    #print(plot_personality_df)

    path_temp_csv = Path.cwd().joinpath('plots_personality_and_ids.csv')
    # index = True star indexing the csv file with 0:
    plot_personality_df.to_csv(path_temp_csv, index = True)

def id_mapping(movielens_ids_list):

    preprocessing_data_csv = Path.cwd().joinpath('preprocessing_data.csv')

    preprocessing_data_df = pd.read_csv(preprocessing_data_csv,
                        sep=",", warn_bad_lines=True, 
                        error_bad_lines=True,
                        engine='python',
                        header=0,
                        usecols = ['movielensId',
                                 'imdbId',
                                 'movie_title',
                                 'year',
                                 'plot']
                                
                        )

    imdb_ids = []

    for id in movielens_ids_list:

        found_object = preprocessing_data_df[preprocessing_data_df['movielensId'] == id]

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

            #movie_imdb_id = 'tt' + movie_imdb_id
            # id is a number
            imdb_ids.append(movie_imdb_id)

            print(imdb_ids)
    
    return imdb_ids

def generate_genre_row(movie_genre_list):

    # dict that relates each tmdb genre name to the indexing position on
    # df columns:

    # 19 default genres:
    tmdb_default_genres = { "Action" : 0, 
                            "Adventure" : 1,
                            "Animation" : 2, 
                            "Comedy" : 3, 
                            "Crime" : 4, 
                            "Documentary" : 5, 
                            "Drama" : 6, 
                            "Family" : 7, 
                            "Fantasy" : 8, 
                            "History" : 9,
                            "Horror" : 10, 
                            "Music" : 11, 
                            "Mystery" : 12, 
                            "Romance" : 13, 
                            "Science Fiction" : 14,
                            "Thriller" : 15,
                            "TV Movie" : 16,
                            "War" : 17,
                            "Western" : 18,
                            "None" : 19 # if couldnt find the genre
                            }

    movie_genre_row = [0] * 20

    for genre in movie_genre_list:
        index_position = tmdb_default_genres[genre]
        movie_genre_row[index_position] = 1
    
    return movie_genre_row

def create_genre_columns():

    plot_personality_csv = Path.cwd().joinpath('plots_personality_and_ids.csv')

    plot_personality_df = pd.read_csv(plot_personality_csv,
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
                                 'openess']
                                
                        )

    Action_column = []
    Adventure_column = [] 
    Animation_column = [] 
    Comedy_column = [] 
    Crime_column = [] 
    Documentary_column = [] 
    Drama_column = [] 
    Family_column = [] 
    Fantasy_column = [] 
    History_column = [] 
    Horror_column = []
    Music_column = [] 
    Mystery_column = []
    Romance_column = [] 
    Science_Fiction_column = []
    Thriller_column = []
    TV_Movie_column = [] 
    War_column = []
    Western_column = []
    None_column = []



    #movies_genre_list = []
    imdb_ids = list(plot_personality_df['imdbId'])

    for id in imdb_ids:
        
        movie_genre_list = TmdbQuery.find_genre(id)
        movie_genre_row = generate_genre_row(movie_genre_list)
        #movies_genre_list.append(movie_genre_list)

        Action_column.append(movie_genre_row[0])
        Adventure_column.append(movie_genre_row[1]) 
        Animation_column.append(movie_genre_row[2])
        Comedy_column.append(movie_genre_row[3])
        Crime_column.append(movie_genre_row[4])
        Documentary_column.append(movie_genre_row[5])
        Drama_column.append(movie_genre_row[6])
        Family_column.append(movie_genre_row[7])
        Fantasy_column.append(movie_genre_row[8])
        History_column.append(movie_genre_row[9])
        Horror_column.append(movie_genre_row[10])
        Music_column.append(movie_genre_row[11])
        Mystery_column.append(movie_genre_row[12])
        Romance_column.append(movie_genre_row[13])
        Science_Fiction_column.append(movie_genre_row[14])
        Thriller_column.append(movie_genre_row[15])
        TV_Movie_column.append(movie_genre_row[16])
        War_column.append(movie_genre_row[17])
        Western_column.append(movie_genre_row[18])
        None_column.append(movie_genre_row[19])
        
    
    
     

    plot_personality_df['Action'] = Action_column 
    plot_personality_df['Adventure'] = Adventure_column
    plot_personality_df['Animation'] = Animation_column
    plot_personality_df['Comedy'] = Comedy_column
    plot_personality_df['Crime'] = Crime_column
    plot_personality_df['Documentary'] = Documentary_column
    plot_personality_df['Drama'] = Drama_column
    plot_personality_df['Family'] = Family_column
    plot_personality_df['Fantasy'] = Fantasy_column
    plot_personality_df['History'] = History_column
    plot_personality_df['Horror'] = Horror_column
    plot_personality_df['Music'] = Music_column
    plot_personality_df['Mystery'] = Mystery_column
    plot_personality_df['Romance'] = Romance_column
    plot_personality_df['Science Fiction'] = Science_Fiction_column
    plot_personality_df['Thriller'] = Thriller_column
    plot_personality_df['TV Movie'] = TV_Movie_column
    plot_personality_df['War'] = War_column
    plot_personality_df['Western'] = Western_column
    plot_personality_df['None'] = None_column


    path_temp_csv = Path.cwd().joinpath('movie_personality_and_genres.csv')
    # index = True star indexing the csv file with 0:
    plot_personality_df.to_csv(path_temp_csv, index = True)


if __name__ == '__main__':

    #movielens_ids_of_final_db()
    create_genre_columns()
    