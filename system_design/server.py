from http.server import HTTPServer, BaseHTTPRequestHandler

# importing the libraries or tools || your requests that youre sending to the server

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

# GET Request that were sending to the server
# status code 200 OK 
# get hello world as a response
# first convert "hello world" to bytes ==> 1,0,0,01,10101010

HTTPServer(("", 8000), Handler).serve_forever()

#  "" 8000

# FastAPI