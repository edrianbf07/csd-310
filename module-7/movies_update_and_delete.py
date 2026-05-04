import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="movies_user",
    password="popcorn",
    database="movies"
)

cursor = db.cursor()

def show_films(cursor, title):


    cursor.execute("""
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS Studio
        FROM film
        INNER JOIN genre
            ON film.genre_id = genre.genre_id
        INNER JOIN studio
            ON film.studio_id = studio.studio_id
    """)

    
    films = cursor.fetchall()

  
    print("\n -- {} --".format(title))

  
    for film in films:

        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}".format(film[3]))
        print()


show_films(cursor, "DISPLAYING FILMS")

#new film
insert_film = """
    INSERT INTO film (
        film_name,
        film_releaseDate,
        film_runtime,
        film_director,
        studio_id,
        genre_id
    )
    VALUES (
        'Inception',
        '2010',
        148,
        'Christopher Nolan',
        1,
        1
    )
"""

cursor.execute(insert_film)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# update Alien to Horror
update_film = """
    UPDATE film
    SET genre_id = 2
    WHERE film_name = 'Alien'
"""

cursor.execute(update_film)
db.commit()

# display after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# delete Gladiator
delete_film = """
    DELETE FROM film
    WHERE film_name = 'Gladiator'
"""

cursor.execute(delete_film)
db.commit()

# display after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()
