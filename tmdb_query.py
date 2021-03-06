import tmdbsimple as tmdb
import requests
import pandas as pd
from pathlib import Path
import key

# preciso colocar no .env:
tmdb.API_KEY = key.tmdb_key

#not working!
def query_by_imdb_id(imdb_id):

    movie_object = tmdb.Find(imdb_id)
    response = movie_object.info()
    print(response)


def query_by_actor(actor_name):

    # lembrar de deixar URI encode
    search = tmdb.Search()
    response = search.person(query = actor_name)
    
    results = response['results']
    actor_id = results[0]['id']
    
    #print("id: ", actor_id)

    actor = tmdb.People(actor_id)
    actor_participations = actor.movie_credits()

    cast = actor_participations['cast']
    
    castings = []
    undisired = ["herself", "himself", "self", actor_name, ""]

    for current_cast in cast:
        
        if current_cast['character'][:4].lower() != "self" and current_cast['character'].lower() not in undisired:

            #print(current_cast['character'][:4])
            cast_item = (current_cast['character'], 
                         current_cast['adult'], 
                         current_cast['title'],  
                         current_cast['genre_ids'],
                         current_cast['vote_average'],
                         current_cast['poster_path'])
            castings.append(cast_item)

    # depois ordenar pelos mais bem rankeados

    best_castings = castings[:3]

    return best_castings

def find_title(imdb_id):

    imdb_id = str(imdb_id)
    find = tmdb.Find(imdb_id)
    response = find.info(external_source='imdb_id')
    print('searching for imdb id: ', imdb_id )
    #print(len(response['movie_results']))

    if len(response['movie_results']) > 0:
        print("titulo encontrado é: ", response['movie_results'][0]['title'])

        found_title = response['movie_results'][0]['title']
        year = response['movie_results'][0]['release_date'][:4]
        
        if year != '':
            year = int(year)
        
        return(found_title, year)
    else:

        return "error", "error"
    
    
def find_genre(imdb_id):

    imdb_id = str(imdb_id)
    find = tmdb.Find(imdb_id)
    response = find.info(external_source='imdb_id')

    id_of_not_found = []
    found = []
    if len(response['movie_results']) > 0:
        #response = query_by_imdb_id(imdb_id)
        genre_ids = response['movie_results'][0]['genre_ids']

        find_genre = tmdb.Genres()
        genres_list = find_genre.movie_list()
        #print(genres_list)
        
    
        for dict in genres_list['genres']:
            if dict['id'] in genre_ids:
                print("dict name", dict['name'])
                found.append(dict['name'])
        
        return found

    else:
        print("error while searching for genres")
        id_of_not_found.append(imdb_id)
        return "None"


    print(id_of_not_found)
    

    #with open("movies_with_genres.txt", 'a+', encoding='utf-8') as f:
        #for movie_id in found:
            #print(movie_id, file=f)

if __name__ == "__main__":

    #query_by_imdb_id('1')
    #teste = query_by_actor('Angelina Jolie')
    #print(teste)

    toy_story_imdb_id = 'tt0114709'

    #error_id = 'tt0112471'
    print(find_title(toy_story_imdb_id))
    #print(find_title(error_id))

    # error is solved:
    #weird_error_unpacking = 'tt0413845'
    #print(find_title(weird_error_unpacking))
    #find_genre('tt0114709')
    #find_genre(weird_error_unpacking)
    