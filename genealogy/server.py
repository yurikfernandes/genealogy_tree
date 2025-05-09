from http.server import HTTPServer

from genealogy.handler import RequestHandler

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class) # Isso cria um socket TCP/IP
    # print(f'Starting server on port {port}...')
    httpd.serve_forever()