import psycopg2
from psycopg2 import Error
try :
    connection = psycopg2.connect(user = "postgres",
    password = "3261848", host = "localhost",
    port = "5432", database = "erfandb")

    cursor = connection.cursor()
    query = ''' select * from car '''
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print("id = ", row[0], )
        print("Manufacturer = ", row[1])
        print("Model = ", row[2])
        print("Price = ", row[3], "\n")
        
except (Exception, psycopg2.Error) as error :
    print ("Error connecting", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed.")

