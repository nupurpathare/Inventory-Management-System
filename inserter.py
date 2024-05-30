import sqlite3

# Connect to the database
connector = sqlite3.connect('inventory.db')
cursor = connector.cursor()

# Sample data to insert (list of tuples)
data_to_insert = [
    (1, 'Laptop', 'High-performance laptop with 4K display', 50, 1299.99),
    (2, 'Smartphone', 'Flagship smartphone with dual cameras', 100, 899.99),
    (3, 'Tablet', 'Thin and lightweight tablet with long battery life', 75, 399.99),
    (4, 'Camera', 'Professional DSLR camera with interchangeable lenses', 30, 1499.99),
    (5, 'Headphones', 'Wireless noise-cancelling headphones with 20-hour battery life', 120, 249.99),
    (6, 'Speaker', 'Bluetooth speaker with rich, immersive sound', 80, 179.99),
    (7, 'Smartwatch', 'Fitness tracker and smartwatch with heart rate monitor', 90, 199.99),
    (8, 'Gaming Console', 'Next-gen gaming console with 4K gaming support', 25, 499.99),
    (9, 'Drone', 'High-quality drone with 4K camera and GPS navigation', 40, 699.99),
    (10, 'VR Headset', 'Virtual reality headset for immersive gaming and experiences', 60, 299.99),
    # Add more data here...
]

# SQL command to insert data into a table
insert_query = """
    INSERT INTO products (p_id, p_name, p_description, p_quantity, p_price)
    VALUES (?, ?, ?, ?, ?)
"""

# Execute the SQL command with executemany()
cursor.executemany(insert_query, data_to_insert)

# Commit the changes to the database
connector.commit()

# Close cursor and connection
cursor.close()
connector.close()

print("Data inserted successfully.")
