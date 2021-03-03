import http.server
import socketserver
import sys 

PORT = 8000
file_to_serve = '/templates/example.xml'

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            print("Sever HIT \n")
            self.path = file_to_serve
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def serve():
    handler_object = MyHttpRequestHandler
    my_server = socketserver.TCPServer(("", PORT), handler_object)
    print(f"Server started at localhost:{PORT} \n")
    my_server.serve_forever()


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        PORT = int(sys.argv[1])
    serve()