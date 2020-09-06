import psycopg2
from psycopg2 import Error
try :
    ''' This section provides the informations 
    required for connecting to the database specified. '''
    connection = psycopg2.connect(user = "postgres",
    password = "*****", host = "localhost",
    port = "5432", database = "erfandb")

    ''' Cursors are used to execute query descriptions'''
    cursor = connection.cursor()
    
    '''query syntaxes can be written in the 
    format of a document string for using it
    in multiline mode '''
    query = ''' select * from car '''
    cursor.execute(query)
    
    '''fetchall command gets every output from 
    the postgres
    cursor.fetchone() fetchs a single row
    cursor.fetchall() fetchs all rows
    cursor.fetchmany(SIZE) fetchs limited rows.
    '''
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

