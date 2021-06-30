from pathlib import Path
import pandas as pd


wiki_plots = Path.cwd().joinpath('archive', 'wiki_movie_plots_deduped.csv')

wiki_plots_df = pd.read_csv (wiki_plots,
                    sep=",", warn_bad_lines=True, 
                    error_bad_lines=True,
                    engine='python',
                    header=0,
                    usecols = ['Release Year',
                               'Title',
                               'Origin/Ethnicity',
                               'Director',
                               'Cast',
                               'Genre',
                               'Wiki Page',
                               'Plot']
                               
                    )

print(wiki_plots_df)