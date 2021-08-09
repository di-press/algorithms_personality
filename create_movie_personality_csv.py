from os import name
from pathlib import Path
import pandas as pd

def create_csv():

    with open('plots_personalities.txt', 'r', encoding='utf-8') as f:
        
        unwanted_chars = [',', '[', ']', ", "]
        movie_personality_info = []

        line = f.readline()

        while line != '': 

            processed_string = ''.join((filter(lambda i: i not in unwanted_chars, line)))
            processed_list = processed_string.split()
            
            movielens_Id = processed_list[0]
            extroversion = int(float(processed_list[1]))
            neuroticism = int(float(processed_list[2]))
            agreeableness = int(float(processed_list[3]))
            conscientiousness = int(float(processed_list[4]))
            openess = int(float(processed_list[5]))                       

            movie_tuple = (movielens_Id, extroversion, neuroticism, agreeableness, conscientiousness, openess)
            #print(movie_tuple, "\n")
            movie_personality_info.append(movie_tuple)

            line = f.readline()

    mapped_plots_df = pd.DataFrame(movie_personality_info,
                      columns = ['movielensId',
                                 'extroversion',
                                 'neuroticism',
                                 'agreeableness',
                                 'conscientiousness',
                                 'openess']
                                )

    # data containing the plots and its personality:
    path_temp_csv = Path.cwd().joinpath('plots_personalities.csv')
    # index = True star indexing the csv file with 0:
    mapped_plots_df.to_csv(path_temp_csv, index = True)

        
        


if __name__=='__main__':
    create_csv()