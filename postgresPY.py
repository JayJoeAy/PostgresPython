import psycopg2
from psycopg2 import Error
try :
    connection = psycopg2.connect(user = "postgres",
    password = "3261848", host = "localhost",
    port = "5432", database = "erfandb")

    cursor = connection.cursor()
    query = ''' Create table mobile (
        ID int primary key not null, 
        model text not null,
        price real
    ); '''
    cursor.execute(query)
    connection.commit()
    print("table created successfully")
except (Exception, psycopg2.Error) as error :
    print ("Error connecting", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed.")

