import psycopg2
'''This file is using the query commands to 
insert data in a table '''
try:
    connection = psycopg2.connect(user = "postgres",
        password = "3261848", host = "localhost",
        port = "5432", database = "erfandb")
    
    cursor = connection.cursor()

    query = '''insert into car (id, make, model, price)
            values (%s, %s, %s, %s) '''
    
    record_to_insert = (1001, 'SAIPA', 'pride', 100)
    cursor.execute(query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if (connection):
        print("Failed inserting data", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("Connection Closed.")