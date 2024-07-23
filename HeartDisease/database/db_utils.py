def create_table(conn, table_name, column_names):

    cursor = conn.cursor()

    # Create a comma-separated list of column definitions
    column_defs = ', '.join([f'{col} TEXT' for col in column_names])

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})
    """)
    conn.commit()


def insert_data(conn, table_name, data):

    cursor = conn.cursor()

    # Get column names from the dictionary keys
    column_names = list(data.keys())

    # Create placeholders for values using question marks
    placeholders = ', '.join(['?'] * len(column_names))

    # Generate the SQL INSERT statement
    sql = f"""INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"""

    # Insert the data using a tuple of values
    cursor.execute(sql, tuple(data.values()))
    conn.commit()


def get_all_data(conn, table_name):

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Convert rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]

    return data
