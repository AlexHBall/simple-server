import http.server
import socketserver
import sys 
PORT = 8000

def serve():
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        PORT = int(sys.argv[1])
    serve()