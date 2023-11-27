import psycopg2
import csv

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur  = conn.cursor()
