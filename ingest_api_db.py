import requests
import psycopg2

with requests.get("http://127.0.0.1:5000/very_large_request/40") as p:
	conn= psycopg2.connect(dbname="stream_database", user= "postgres", password= "mydatabase")
	cur= conn.cursor()
	sql= "INSERT INTO transaction (txid, uid, amount) VALUES(%s, %s, %s)"


	buffer= ""
	for chunk in p.iter_content(chunk_size= 1):
		if chunk.endswith(b'\n'):
			t= eval(buffer)
			print(t)
			cur.execute(sql,(t[0],t[1], t[2]))
			conn.commit()
			buffer= ""
		else:
			buffer+= chunk.decode()