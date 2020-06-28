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
            <link href="/static/css/styles.css" rel="stylesheet">
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
        filter = (data['genre'] == genre) & (data['year'] > year) & (data['avg_vote'] > 7) & (data['votes'] < 1000)

        filtered = data[filter]
        titles = list(filtered['title'])
        pick1 = random.choice(titles)
        titles.remove(pick1)
        pick2 = random.choice(titles)
        titles.remove(pick2)
        pick3 = random.choice(titles)

        return """<html>
        <head>
            <link href="/static/css/styles.css" rel="stylesheet">
        </head>        
        <body>
        <table class="table">
          <tr>
            <th>Title</th>
            <th>Country</th>
            <th>Rating</th>
          </tr>
          <tr>
            <td>%(pick1)s</td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td>%(pick2)s</td>
            <td></td>
            <td></td>
          </tr>      
          <tr>
            <td>%(pick3)s</td>
            <td></td>
            <td></td>
          </tr>
        
        </body>
        
        </html>""" %{"pick1": pick1, "pick2": pick2, "pick3":pick3}


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
    cherrypy.quickstart(MoviePicker())