import mysql.connector
import requests
import json
import keyring
import getpass

service_name = "mysql"
username = "root"

# Call Password
password = keyring.get_password(service_name, username)

# If Password not set
if not password:
    # Password not saved right now
    while True:
        pw = getpass.getpass("MySQL Passwort eingeben: ")
        if not pw:
            print("Passwort darf nicht leer sein!")
            continue
        keyring.set_password(service_name, username, pw)
        mysql_password = pw
        print("Passwort im Keyring gespeichert.")
        break

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=username,
    password=password,
    database="database"
)

cursor = conn.cursor(dictionary=True)

# Fetch Data Example
cursor.execute("SELECT * FROM customers LIMIT 15")
rows = cursor.fetchall()

# Close Connection
cursor.close()
conn.close()

# Send Data to API
url = "INSERT HERE THE URL TO THE API"

headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, data=json.dumps(rows, default=str))

#  Response
print("Status Code:", response.status_code)
print("Antwort JSON:", response.text)