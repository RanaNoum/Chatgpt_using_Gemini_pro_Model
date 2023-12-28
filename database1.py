import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='nomi12345',
        database='my_first_db'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the chat_history table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_input TEXT,
                model_response TEXT
            )
        ''')

        print("Database connection established successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Function to insert chat history into the database
def insert_chat_history(user_input, model_response):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nomi12345',
            database='my_first_db'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = "INSERT INTO chat_history (user_input, model_response) VALUES (%s, %s)"
            data = (user_input, model_response)
            cursor.execute(insert_query, data)
            connection.commit()

            print("Chat history inserted successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to retrieve chat history from the database
def get_chat_history():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nomi12345',
            database='my_first_db'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            select_query = "SELECT user_input FROM chat_history ORDER BY id DESC"
            cursor.execute(select_query)
            results = cursor.fetchall()

            chat_history = []
            for row in results:
                chat_history.append(row[0])

            print("Chat history retrieved successfully.")

            return chat_history

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
