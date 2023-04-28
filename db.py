import psycopg2

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="crud",
            user="postgres",
            password='user',
            host='localhost'
        )
        print('db connected')
        return connection
    except(e):
        print("db connection error: " , e.message)

#db = connection.cursor()
#db.execute('SELECT * FROM USERS')
#print(db.fetchall())