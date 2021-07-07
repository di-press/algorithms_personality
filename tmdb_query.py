
import tmdbsimple as tmdb
import requests

# preciso colocar no .env:
tmdb.API_KEY = '5225e0599ef4dcff1d23b22faa1af8ed'

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

def find_exemplo():
    find = tmdb.Find('tt0120363')
    response = find.info(external_source='imdb_id')
    print(response)

if __name__ == "__main__":

    #query_by_imdb_id('1')
    #teste = query_by_actor('Angelina Jolie')
    #print(teste)

    find_exemplo()