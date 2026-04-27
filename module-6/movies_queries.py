import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cr7andm10!!!",
    database="movies"
)

cursor = db.cursor()

#Studio
print("-- DISPLAYING studio RECORDS --")
cursor.execute("SELECT studio_id, studio_name FROM studio")

studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}".format(studio[0]))
    print("Studio Name: {}\n".format(studio[1]))


#Genre 
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT genre_id, genre_name FROM genre")

genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}".format(genre[0]))
    print("Genre Name: {}\n".format(genre[1]))



print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

films = cursor.fetchall()
for film in films:
    print("Film Name: {}".format(film[0]))  
    print("Runtime: {}\n".format(film[1]))



print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

directors = cursor.fetchall()
for director in directors:
    print("Film Name: {}".format(director[0]))
    print("Director: {}\n".format(director[1]))
