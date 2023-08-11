import psycopg2

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432",
        )
        print("Connection to PostgreSQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")