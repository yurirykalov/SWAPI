# test DB connection
import datetime
import psycopg
from psycopg.types.json import Jsonb
from utils.swapi import  APIRequester

base_url = 'https://swapi.py4e.com/api/'
end_point = 'people/1'

api = APIRequester(base_url)

people_data = api.get(end_point).json()


conn = psycopg.connect(
    host='localhost',
    port=5432,
    dbname='swapi',
    user='admin',
    password='admin123'
)

cur = conn.cursor()

cur.execute("""
    INSERT INTO stg.people (id, payload, updated_ts)
            VALUES (%s, %s, %s)
""", (1, Jsonb(people_data), datetime.datetime.now()))

conn.commit()




