import psycopg2

def getCarDetails(carID):
    try:
        connection = psycopg2.connect(user = "postgres",
        password = "3261848", host = "localhost",
        port = "5432", database = "erfandb")

        cursor = connection.cursor()
        query = "select * from car where id = %s"
        
        cursor.execute(query, (carID,))
        records = cursor.fetchall()
        for row in records:        
            print("id = ", row[0], )
            print("Manufacturer = ", row[1])
            print("Model = ", row[2])
            print("Price = ", row[3], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error Fetching data from PostgresQL table", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("Connection closed. \n")
        
    
getCarDetails(62)
getCarDetails(3)
