from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parseando a URL apenas quando necessário (aqui dentro do método)
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)
        
        print(f"URL: {url}")
        print(f"Path: {path}")
        print(f"Query: {query}")
        
        # Handle GET request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
    
    def do_POST(self):
        # Handle POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f'Received POST data: {post_data.decode("utf-8")}')
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST request received!')

# Implementar rotas do servidor