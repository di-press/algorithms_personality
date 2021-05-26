class UserItem:

    def __init__(self, hash_id, movies, big_five):
        
        self.hash_id = hash_id
        self.movies = movies
        self.extroversion = big_five['extroversion']
        self.neuroticism = big_five['neuroticism']
        self.agreeableness = big_five['agreeableness']
        self.conscientiousness = big_five['conscientiousness']
        self.openess = big_five['openess']