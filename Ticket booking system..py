import mysql.connector

# Establish a database connection
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="zayed@107119",
        database="project",
        auth_plugin='mysql_native_password'
    )

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    def insert_movie(name, rating, language, genre, theatre, last_date, price):
        sql = "INSERT INTO MOVIES (NAME, RATING, LANGUAGE, GENRE, THEATRE, TICKET_PRICE, LAST_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, rating, language, genre, theatre, price, last_date)
        mycursor.execute(sql, values)
        mydb.commit()

    def remove_movie(movie_name):
        sql = "DELETE FROM MOVIES WHERE NAME = %s"
        mycursor.execute(sql, (movie_name,))
        mydb.commit()

    def update_movie_ticket_price(movie_name, new_price):
        sql = "UPDATE MOVIES SET TICKET_PRICE = %s WHERE NAME = %s"
        mycursor.execute(sql, (new_price, movie_name))
        mydb.commit()

    def list_movies():
        sql = "SELECT NAME, RATING, LANGUAGE, GENRE, THEATRE, TICKET_PRICE, LAST_DATE FROM MOVIES"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for row in result:
            print("Name:", row[0])
            print("Rating:", row[1])
            print("Language:", row[2])
            print("Genre:", row[3])
            print("Theatre:", row[4])
            print("Ticket Price:", row[5])
            print("Last Date:", row[6])
            print("\n")

    def book_ticket(movie_name, num_tickets):
        try:
            # Check if the movie exists
            check_sql = "SELECT TICKET_PRICE FROM MOVIES WHERE NAME = %s"
            mycursor.execute(check_sql, (movie_name,))
            result = mycursor.fetchone()

            if not result:
                return f"Movie '{movie_name}' does not exist."

            ticket_price = result[0]

            # Calculate the total price for the tickets
            total_price = ticket_price * num_tickets

            # Insert a booking record into the database
            book_sql = "INSERT INTO BOOKINGS (MOVIE_NAME, NUM_TICKETS, TOTAL_PRICE) VALUES (%s, %s, %s)"
            book_values = (movie_name, num_tickets, total_price)
            mycursor.execute(book_sql, book_values)
            mydb.commit()

            return f"Successfully booked {num_tickets} ticket(s) for '{movie_name}' for a total of ${total_price}."

        except mysql.connector.Error as err:
            return f"Error: {err}"

    def theatre(theatre_name):
        try:
            # Retrieve theater information from the database
            theatre_info_sql = "SELECT NAME, SEAT_COUNT FROM THEATRES WHERE NAME = %s"
            mycursor.execute(theatre_info_sql, (theatre_name,))
            theatre_info = mycursor.fetchone()

            if not theatre_info:
                return f"Theater '{theatre_name}' does not exist."

            # Retrieve the number of booked seats for the theater
            booked_seats_sql = "SELECT SUM(NUM_TICKETS) FROM BOOKINGS WHERE MOVIE_NAME IN (SELECT NAME FROM MOVIES WHERE THEATRE = %s)"
            mycursor.execute(booked_seats_sql, (theatre_name,))
            booked_seats = mycursor.fetchone()

            if booked_seats[0] is None:
                booked_seats_count = 0
            else:
                booked_seats_count = booked_seats[0]

            # Calculate the number of remaining seats
            remaining_seats = theatre_info[1] - booked_seats_count

            # Retrieve movie play count and timings
            movie_play_count_sql = "SELECT COUNT(DISTINCT NAME) FROM MOVIES WHERE THEATRE = %s"
            mycursor.execute(movie_play_count_sql, (theatre_name,))
            movie_play_count = mycursor.fetchone()[0]

            movie_timings_sql = "SELECT DISTINCT LAST_DATE FROM MOVIES WHERE THEATRE = %s"
            mycursor.execute(movie_timings_sql, (theatre_name,))
            movie_timings = mycursor.fetchall()

            return f"Theater: {theatre_info[0]}\n" \
                   f"Total Seats: {theatre_info[1]}\n" \
                   f"Booked Seats: {booked_seats_count}\n" \
                   f"Remaining Seats: {remaining_seats}\n" \
                   f"Number of Times Movie Plays: {movie_play_count}\n" \
                   f"Movie Timings: {', '.join(str(t[0]) for t in movie_timings)}"

        except mysql.connector.Error as err:
            return f"Error: {err}"

    # Example usage:
    insert_movie("Movie1", "PG-13", "English", "Action", "Theatre1", "2023-12-31", 40.0)
    insert_movie("Movie2", "R", "Spanish", "Comedy", "Theatre2", "2023-12-30", 40.0)
    list_movies()
    update_movie_ticket_price("Movie1", 45.0)
    update_movie_ticket_price("Movie3", 50.0)
    remove_movie("Movie2")
    book_result = book_ticket("Movie2", 4)
    print(book_result)

    # Example usage of the 'theatre' function
    theatre_info = theatre("Theatre1")
    print(theatre_info)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the database connection when done
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
