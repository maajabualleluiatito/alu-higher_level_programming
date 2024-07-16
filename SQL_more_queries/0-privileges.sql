import mysql.connector

# MySQL connection details
host = 'localhost'
admin_user = 'admin'
admin_password = 'admin_password'

# Users to check privileges for
users = ['user_0d_1', 'user_0d_2']

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host=host,
    user=admin_user,
    password=admin_password
)

# Create a cursor object
cursor = conn.cursor()

# Function to retrieve and print privileges for a given user
def print_user_privileges(username):
    query = f"SHOW GRANTS FOR '{username}'@'localhost';"
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"Privileges for {username}:")
    for row in results:
        print(row[0])
    print()

# Loop through the users and print their privileges
for user in users:
    print_user_privileges(user)

# Close the cursor and connection
cursor.close()
conn.close()
