

import requests
import json


def get_id(title):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"page": "1", "r": "json", "s": title}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "ac9d9266admshaccf7fc1e5ab755p1de0dajsnd7d6e7d5ef79"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.content)
    datafinal=(data['Search'][0])
    id = datafinal['imdbID']
    return id

def get_rating(id):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i":id,"r":"json"}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "ac9d9266admshaccf7fc1e5ab755p1de0dajsnd7d6e7d5ef79"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.content)
    rating = (data['imdbRating'])
    year = (data['Year'])
    genre = (data['Genre'])
    runtime=(data['Runtime'])
    return [rating,year,genre,runtime]

#title = input("Digite o nome do filme: ")
#print(get_rating(get_id(title)))

