class Movie:
    #big_five is a dict
    def __init__(self, movie_id, movie_name, movie_rating, movie_script, big_five, genre):
        
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_rating = movie_rating
        self.movie_script = movie_script
        self.extroversion = big_five['extroversion']
        self.neuroticism = big_five['neuroticism']
        self.agreeableness = big_five['agreeableness']
        self.conscientiousness = big_five['conscientiousness']
        self.openess = big_five['openess']
        self.genre = genre