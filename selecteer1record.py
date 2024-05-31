POSTGRES_NAME = (
    "postgreseigen"  # change this to the name of your Postgres application
)
POSTGRES_NAMESPACE = (
    "henk-huijgen"  # change this to the namespace of your Postgres application
)
POSTGRES_HOST = f"postgres-{POSTGRES_NAME}.{POSTGRES_NAMESPACE}"

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create a database
# (Optional: create this database with a configuration script as described above)
connection = psycopg2.connect(host=POSTGRES_HOST, user="postgres", password="postgres")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
# cursor.execute("CREATE DATABASE eigendatabase")

# Insert data into our new database
# (Optional: insert this data with a configuration script as described above)
# with psycopg2.connect(
#     host=POSTGRES_HOST, user="postgres", password="postgres", database="eigendatabase"
# ) as connection:
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "CREATE TABLE tableeigen (id SERIAL PRIMARY KEY, name TEXT NOT NULL, count INT NOT NULL)"
#         )
#         cursor.execute(
#             "INSERT INTO tableeigen (name, count) VALUES ('atitle', 1), ('anothertitle', 2), ('somethingdifferent', 3)"
#         )

# Select data
with psycopg2.connect(
    host=POSTGRES_HOST, user="postgres", password="postgres", database="eigendatabase"
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM tableeigen WHERE name ~ '.*title.*'")
        for row in cursor.fetchall():
            print(row)

connection.close()