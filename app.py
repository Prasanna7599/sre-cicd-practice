from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b"Hello from my own container!")
HTTPServer(("0.0.0.0", 8000), Handler).server_forever()
