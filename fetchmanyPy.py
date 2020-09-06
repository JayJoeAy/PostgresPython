import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
        password = "3261848", host = "localhost",
        port = "5432", database = "erfandb")

    print("Selecting rows from mobile table using cursor.fetchall")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from car"

    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchmany(5)
    
    print("Printing 2 rows")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[2])
        print("Price  = ", row[3], "\n")

    mobile_records = cursor.fetchmany(2)
    
    print("Printing next 2 rows")
    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[2])
        print("Price  = ", row[3], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")