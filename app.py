import random
import os, os.path
import string
import pandas as pd
import cherrypy


data = pd.read_csv("IMDb-movies.csv")



class MoviePicker(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>            
            <link href="/static/css/styles.css " rel="stylesheet">
           </head>
          <body>
            <h1>Secret Movie Picker</h1>
            <form method="get" action="generate">
              <label for="genre">Type the gender that you like to watch:</label>
              <select name="genre">
                <option value="Drama"> Drama </option>
                <option value="Comedy"> Comedy </option>
                <option value="Horror"> Horror </option>
                <option value="Romance"> Romance </option>

              </select> <br>
               
              <label for="year">Type the max year of release to the movie: </label>
              <input type="range" min="1950" value="1950" max="2010" name="year" oninput = "display.value=value" onchange="display.value=value">
              <input type="text"id="display" value = "1950" readonly > <br>
              <button type="submit">Pick a movie</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self,genre, year):
        year = int(year)
        filter = (data['genre'] == genre) & (data['year'] < year) & (data['avg_vote'] > 7) & (data['votes'] < 1000)
        #parameteres filter
        filtered = data[filter]
        titles = list(filtered['title'])
        #PICK1
        pick1 = random.choice(titles)
        pick1filter = (data['title'] == pick1)
        choice = data[pick1filter]
        country1=choice['country'].values.astype(str)
        description1 = choice['description'].values.astype(str)
        link1 = "https://www.imdb.com/title/"+choice['imdb_title_id'].values

        #PICK2
        pick2 = random.choice(titles)
        pick2filter = (data['title'] == pick2)
        choice2 = data[pick2filter]
        country2 = choice2['country'].values.astype(str)
        description2 = choice2['description'].values.astype(str)
        link2 = "https://www.imdb.com/title/"+choice2['imdb_title_id'].values

        titles.remove(pick2)

        #PICK3
        pick3 = random.choice(titles)
        pick3filter = (data['title'] == pick3)
        choice3 = data[pick3filter]
        country3 = choice3['country'].values.astype(str)
        description3 = choice3['description'].values.astype(str)
        link3 = "https://www.imdb.com/title/"+choice3['imdb_title_id'].values


        return """<html>
        <head>
            <link href="/static/css/styles.css"   rel="stylesheet">
        </head>        
        <body>
        <table class="table">
          <tr>
            <th>Title</th>
            <th>Country</th>
            <th>Description</th>
          </tr>
          <tr>
            <td><a href="%(link1[0])s" target = "blank">%(pick1)s</a></td>
            <td>%(country1[0])s</td>
            <td>%(description1[0])s</td>
          </tr>
          <tr>
            <td><a href="%(link2[0])s" target = "blank">%(pick2)s</a></td>
            <td>%(country2[0])s</td>
            <td>%(description2[0])s</td>
          </tr>      
          <tr>
            <td><a href="%(link3[0])s" target = "blank">%(pick3)s</a></td>
            <td>%(country3[0])s</td>
            <td>%(description3[0])s</td>
          </tr>
        
        </body>
        
        </html>""" %{"pick1": pick1, "pick2": pick2, "pick3":pick3,
                     "description1[0]":description1[0], "country1[0]":country1[0],"description2[0]":description2[0],
                     "country2[0]":country2[0],"description3[0]":description3[0], "country3[0]":country3[0],
                     "link1[0]":link1[0],"link2[0]":link2[0],"link3[0]":link3[0]}


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(MoviePicker(), '/', conf)