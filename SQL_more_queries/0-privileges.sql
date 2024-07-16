# ahfbviasfbhviasfv

import mysql.connector

# MySQL connection details
host = 'localhost'
admin_user = 'admin'  # Replace with your MySQL admin username
admin_password = 'admin_password'  # Replace with your MySQL admin password

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

# Function to retrieve privileges for a given user
def get_user_privileges(username):
    query = f"SHOW GRANTS FOR '{username}'@'localhost';"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.errors.ProgrammingError:
        return None

# Function to determine the type of privileges for a user
def determine_privileges(privileges):
    if not privileges:
        return None

    for privilege in privileges:
        if 'ALL PRIVILEGES' in privilege[0]:
            return 'root'
        if 'SELECT' in privilege[0] and 'INSERT' in privilege[0]:
            return 'select_insert'

    return 'other'

# Retrieve and print the privileges for each user
user_privileges = {}
for user in users:
    privileges = get_user_privileges(user)
    if privileges is not None:
        user_privileges[user] = determine_privileges(privileges)
    else:
        user_privileges[user] = None

# Determine the correct output based on retrieved privileges
if all(privilege is None for privilege in user_privileges.values()):
    print("Users don’t exist")
elif user_privileges['user_0d_1'] == 'root' and user_privileges['user_0d_2'] is None:
    print("user_0d_1 root user")
elif user_privileges['user_0d_1'] == 'root' and user_privileges['user_0d_2'] == 'root':
    print("user_0d_1 and user_0d_2 root users")
elif user_privileges['user_0d_1'] == 'root' and user_privileges['user_0d_2'] == 'select_insert':
    print("user_0d_1 root user and user_0d_2 SELECT and INSERT privileges of the database user_2_db")
else:
    print("Privileges do not match expected cases")

# Close the cursor and connection
cursor.close()
conn.close()

