import pandas as pd
import random



data = pd.read_csv("IMDb-movies.csv")

genre = input("Type the gender that you like to watch: ")
year = int(input("Type the max year of release to the movie: "))
#country = input("What country is the movie from? ")

try:
    filter = (data['genre'] == genre) & (data['year'] > year)  & (data['avg_vote']>7) & (data['votes']<1000)

    filtered = data[filter]
    titles = list(filtered['title'])
    #print(filtered.shape)
    print(random.sample(titles,3))
except ValueError:
    print("Oups, sorry, I'm a dumb robot, I was not able to find a good movie with this parameters")
    print()
    print("So... ")
    print('......')
    opt =input("If you like I can display you some older movies, type yes if you liked this idea: ")
    if opt == 'yes' or opt == 'Yes' or opt == 'Y' or opt == 'y':
        filter = (data['genre'] == genre) & (data['year'] > 2000) & (
                    data['avg_vote'] > 7) & (data['votes'] < 1000)
        filtered = data[filter]
        titles = list(filtered['title'])
        #print(filtered.shape)
        print(random.sample(titles, 3))


