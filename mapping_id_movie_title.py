from pathlib import Path
import pandas as pd
import movielens_id_title as Mv
import map_movielens_tmdb_id as MapIds
import tmdb_query as TmdbQuery
import title_and_plots as TitlePlots

def find_titles_test(tuple_of_ids):

    tuple_ids_and_titles_and_year = []

    limit = 0


            
    for item in tuple_of_ids:

        imdb_id = item[1]
        title, year = TmdbQuery.find_title(imdb_id)

        if title != 'error':
            new_item = (item[0], item[1], str(title), year)
            tuple_ids_and_titles_and_year.append(new_item)
            limit += 1

            if limit>10:
                break

    
    return tuple_ids_and_titles_and_year



def find_titles(tuple_of_ids):

    tuple_ids_and_titles_and_year = []

    for item in tuple_of_ids:

        imdb_id = item[1]
        title, year = TmdbQuery.find_title(imdb_id)

        if title != 'error':
            new_item = (item[0], item[1], str(title), year)
            tuple_ids_and_titles_and_year.append(new_item)
    
    return tuple_ids_and_titles_and_year


def find_all_plots(ids_and_titles_year_tuples):

    all_movies_plots = []

    plots_df = TitlePlots.create_df()

    for item in ids_and_titles_year_tuples:
        movie_title = item[2]
        year = int(item[3])

        plot = TitlePlots.find_plot(plots_df, movie_title, year)

        if plot != 'error':

            new_item = (item[0], item[1], item[2], item[3], plot)
            all_movies_plots.append(new_item)

    return all_movies_plots

def generate_csv_database(tuples_titles_and_plot):

    mapped_plots_df = pd.DataFrame(tuples_titles_and_plot,
                      columns = ['movieId',
                                 'imdbId',
                                 'tmdbId',
                                   ''])

def create_database_test():

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

    link_df = MapIds.create_link_df()
    movielens_imdb_ids_tuples = MapIds.find_tmdb_id(all_movies, link_df)
    #print(movielens_imdb_ids_tuples)

    ids_and_titles_year_tuples = find_titles_test(movielens_imdb_ids_tuples)
    #print(ids_and_titles_year_tuples)
    
    tuples_titles_and_plot = find_all_plots(ids_and_titles_year_tuples)
    
    print(tuples_titles_and_plot)
    print("dos 10 filmes, foram encontrados: ", len(tuples_titles_and_plot))


if __name__ == '__main__':

    create_database_test()
    