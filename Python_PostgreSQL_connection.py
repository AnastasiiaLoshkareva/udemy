# Install PostgreSQL
# Create DB = 'scheduler_db' and table = 'events' through pgAdmin4
# Connect python to DB

import psycopg2

# Connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'scheduler_db',
    'user': 'postgres',
    'password': '0409'
}

try:
    # Establish connection
    conn = psycopg2.connect(**db_params)

    # Create a cursor
    cursor = conn.cursor()

    # Get table names from the 'information_schema.tables' view
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public';
    """)
    
    # Fetch all table names
    table_names = cursor.fetchall()

    # Print table names
    print("Table Names:")
    for table in table_names:
        print(table[0])

    cursor.execute("SELECT * FROM events")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print(row)
        
    # Close cursor
    cursor.close()

except psycopg2.OperationalError as e:
    print(f"Error: {e}")

finally:
    # Close connection
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    main()
