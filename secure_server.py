# secure_server.py
import http.server
import ssl

server_address = ('0.0.0.0', 4443)

# HTTP server
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# SSL context yaratish
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# Client sertifikati talab qilinadi
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile='ca/rootCA.crt')

# HTTP serverni SSL bilan o‘rash
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running on https://0.0.0.0:4443")
httpd.serve_forever()
