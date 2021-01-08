'''
Created on Jan 5, 2021

@author: Alex Kim

Analyzed a movie metadata set allowing users to observe trends between a 
director's films and the film's respective IDMB Scores
'''
#Importing needed packages
import pandas as pd
import plotly.express as px

#Read in movie data set
df = pd.read_csv('movie_metadata.csv')
df = df.dropna()
#Asking user to input a Director's name
director1 = raw_input("What Director's work would you like to analyze? ")

#Subsetting data to only show films directed by the given director
directorWork = df[df.director_name == director1]

#Creates a bar chart to show the relationship between films and film IMDB scores
fig = px.bar(df, x = directorWork.movie_title, y = directorWork.imdb_score,
          hover_name = directorWork.movie_title,
          color = directorWork.imdb_score,
          title = '{} Films vs. {} Film IMDB Scores'.format(director1, director1),
          labels = {'x' : '{} Movie'.format(director1), 'y' : 'IMDB Score'},
          text = directorWork.imdb_score
          )
fig.update_traces(hoverinfo = 'skip', hovertemplate = None, textposition = 'outside')
#Prints the bar chart
print(fig.show())

#Finds the movie with the highest rating and the movie with the lowest rating
bmIndex = directorWork.imdb_score.sort_values(ascending = False).head(1).index[0]
bestMovie = df.iloc[bmIndex].movie_title
bmScore = df.iloc[bmIndex].imdb_score
wmIndex = directorWork.imdb_score.sort_values().head(1).index[0]
worstMovie = df.iloc[wmIndex].movie_title
wmScore = df.iloc[wmIndex].imdb_score

#prints the director's highest rated film and the director's lowest rated film
print("{}'s highest rated film is {} with an IMDB score of {}".format(director1, str(bestMovie), str(bmScore)))
print("{}'s lowest rated film is {} with an IMDB score of {}".format(director1, str(worstMovie), str(wmScore)))
