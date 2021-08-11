from pathlib import Path
import pandas as pd


class UserItem:
    #big five is a dict; movies is a list with Movie objects

    def __init__(self, hash_id, movies, big_five):
        
        self.hash_id = hash_id
        self.movies = movies
        self.extraversion = big_five['extraversion']
        self.emotional_stability = big_five['emotional_stability']
        self.agreeableness = big_five['agreeableness']
        self.conscientiousness = big_five['conscientiousness']
        self.openess = big_five['openess']

    def print_user(self):

        print("user: \n")
        print("id: ", self.hash_id)
        print("movies: ", self.movies)
        print("extraversion: ", self.extraversion)
        print("emotional_stb: ",  self.emotional_stability)
        print("agreeableness :", self.agreeableness)
        print("conscientiousness: ", self.conscientiousness)
        print("openess: ", self.openess)
        