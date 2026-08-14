import psycopg2

#establishing db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='Emali50',dbname='ecommerce')

#creating a cursor object to perform db operations
cur = conn.cursor