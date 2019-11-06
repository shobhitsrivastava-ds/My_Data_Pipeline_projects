from flask import Flask
import time
import uuid
from flask import Response
import random
from flask import stream_with_context

app= Flask(__name__)

@app.route("/very_large_request/<int:rowcount>", methods= ["GET"])
def get_large_request(rowcount):
	"""return the n nows of data"""
	def f():
		""" The generator of mock data"""
		for _i in range(rowcount):
			time.sleep(0.012)
			txid= uuid.uuid4()
			uid= uuid.uuid4()
			amount= round(random.uniform(-1000,1000),2)
			yield f"('{txid}', '{uid}',{amount})\n"
	return Response(stream_with_context(f()))

if __name__=="__main__":
	app.run(debug= True)