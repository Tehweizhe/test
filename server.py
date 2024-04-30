from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from scraper import scrape_the_verge

class SimpleHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/headlines':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            headlines = scrape_the_verge()
            self.wfile.write(json.dumps(headlines).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('background.html', 'rb') as file:
                self.wfile.write(file.read())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPServer)
    print(f'Server is running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

