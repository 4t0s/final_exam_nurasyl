# import requests
# import json
import sqlite3
# import datetime
# import random

connection = sqlite3.connect('cinema_store.db')

cursor = connection.cursor()

# url = "https://imdb-top-100-movies.p.rapidapi.com/"

# headers = {
# 	"X-RapidAPI-Key": "ad761c6685msh23982c33ec09642p1e22b5jsn8e6e7a7adec0",
# 	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# with open('movies.json', 'w') as file:
#     file.write(json.dumps(response.json(), indent = 4))
    
# movies = response.json()

# for movie in movies:
#     print(movie.get('title', 'Unknown'))
    
#     name = movie.get('title', 'Unknown')
#     genre = movie.get('genre', 'Unknown')[0]
#     year = movie.get('year', 'Unknown')
#     description = movie.get('description', 'Unknown')
#     rating = float(movie.get('rating', 'Unknown'))
    
#     name = name.replace('"', "'")
#     description = description.replace('"', "'")
#     genre = genre.replace('"', "'")
    
#     cursor.execute(
#         f'INSERT INTO afisha (name, genre, year, description, rating) VALUES ("{name}","{genre}",{year},"{description}",{rating})')
#     connection.commit()
    
# cinemas = [
#     {
#         'name':'Eurasia Cinema 7',
#         'address': 'Kazan Mamaev st.,  11/1'
#     },
#     {
#         'name':'Chaplin Cinemas',
#         'address': 'Bolshoy Morskoi pereulok, d.1'
#     },
#     {
#         'name':'Arman',
#         'address': 'Lenina, 33'
#     },
#     {
#         'name':'Kinopark',
#         'address': 'Tverskaya ul., 56'
#     },
#     {
#         'name':'Arsenal',
#         'address': 'Prospect Mira str., 28'
#     },
# ]

# for cinema in cinemas: 
#     name = cinema.get('name', 'Unknown') 
#     address = cinema.get('address', 'Unknown') 
 
#     name = name.replace('"', "'") 
#     address = address.replace('"', "'") 
 
#     cursor.execute(f'INSERT INTO cinema (name, address) VALUES ("{name}", "{address}")') 
#     connection.commit() 


# start_date = datetime.date.today()
# start_time = start_date.strftime("%H:%M:%S")
# end_date = datetime.date(2024, 5, 30)
# end_time = end_date.strftime("22:00:00")
# gap = int((end_date - start_date).total_seconds())
# movies_id = [random.randint(1, 100) for i in range(1, 51)]
# cinemas_id = [random.randint(1, 100) for i in range(1, 51)]
# prices = [random.randint(1000, 5000) for i in range(1, 51)]
# dates = [start_date + datetime.timedelta(seconds = random.randint(0, gap)) for i in range(1, 51)]
# time = [f"{random.randint(16,23)}:{random.randint(0,5)}0:00"for i in  range(1, 51)]
# capacities = [random.randint(50, 100) for  i in range(1, 51)]

# for i in range(0, 50):
#     cursor.execute(
#         f'INSERT INTO admin_afisha (movie_id, cinema_id, price, date, time, capacity) VALUES({movies_id[i]},{cinemas_id[i]},{prices[i]},"{dates[i]}","{time[i]}",{capacities[i]})'
#     )
#     connection.commit()


# afishas = [i for i in range(1, 51)]
# rooms = [random.randint(1, 6) for i in range(1,51)]
# rows = [random.randint(1, 16) for i in range(1,51)]
# columns = [random.randint(1, 16) for i in range(1,51)]

# for i in range(0 ,50):
#     cursor.execute(
#         f'insert into place (afisha_id, room, row, seat) VALUES ({afishas[i]}, {rooms[i]}, {rows[i]}, {columns[i]})'
#     )
#     connection.commit()