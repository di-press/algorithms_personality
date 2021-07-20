from pathlib import Path
import pandas as pd


def create_df():

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

    
    return wiki_plots_df.copy(deep=True)


def find_plot(df, movie_title, year):

        print("procurando a plot do filme: ", movie_title)
        year = int(year)
        #found_object = df[df["Title"] == movie_title and df['Release Year'] == year]
        found_object = df.query('Title == @movie_title and `Release Year` == @year')
        #found_object = df[df["Title"] == movie_title]
        #found_object = df.query('Title == movie_title')

        print('found object: ', found_object.iloc[0]['Plot'])
        #print(type(found_object.iloc[0]['Plot']))
        
        
        if not found_object.empty:
            #plot = str(found_object['Plot'].item())
            plot = str(found_object.iloc[0]['Plot'])

            # removing '\', '\n' and '\r' of the plots: 
            plot = plot.strip()
            if len(plot) > 0:
                return plot
        else:
            return 'error'
            
if __name__ == '__main__':

    df = create_df()
    #plot = find_plot(df, 'Heat', 1995)
    #plot = find_plot(df, 'The Fighter', 2010)
    plot = find_plot(df, 'Happy Feet', 2006)
    print(plot)

