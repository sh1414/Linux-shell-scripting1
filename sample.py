from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(f"""
        <html>
            <body>
                <h1>Container IP Address</h1>
                <p>Hostname: {hostname}</p>
                <p>IP Address: {ip_address}</p>
            </body>
        </html>
        """.encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Server running on port 8080...")
server.serve_forever()
