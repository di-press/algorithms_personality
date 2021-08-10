from pathlib import Path
import pandas as pd
import map_movielens_imdb_id 

#personality_csv_file = Path.cwd().joinpath('personality-isf2018', 'personality-data.csv')
#movie_dat_file = Path.cwd().joinpath('tag-genome', 'movies.dat')

# 

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

    path_temp_csv = Path.cwd().joinpath('plots_personality2.csv')
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

            movie_imdb_id = 'tt' + movie_imdb_id
            # id is a number
            imdb_ids.append(movie_imdb_id)

            #print(movie_title)
    
    return imdb_ids


def print_genres():

    plot_personality_csv = Path.cwd().joinpath('plots_personality2.csv')

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

    imdb_ids = list(plot_personality_df['imdbId'])

    print(imdb_ids)


if __name__ == '__main__':

    #print(movielens_ids_of_final_db())
    print_genres()
    