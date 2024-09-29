import psycopg2
from psycopg2 import sql

# PostgreSQL connection details
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "conversations"
DB_USER = "postgres"
DB_PASSWORD = "5607"

# Create a PostgreSQL connection
def create_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Create table for storing conversation data
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation (
            id SERIAL PRIMARY KEY,
            caller_name VARCHAR(255),
            conversation_id UUID,
            transcript TEXT
        );
    ''')
    conn.commit()
    conn.close()

# Insert conversation data into PostgreSQL
def insert_conversation(caller_name, conversation_id, transcript):
    conn = create_connection()
    cursor = conn.cursor()
    query = sql.SQL("INSERT INTO conversation (caller_name, conversation_id, transcript) VALUES (%s, %s, %s)")
    cursor.execute(query, (caller_name, conversation_id, transcript))
    conn.commit()
    conn.close()
