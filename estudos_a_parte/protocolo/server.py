from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Contet-Type", "text/html; charset=utf-8")
            self.send_header("Teste","abc")
            self.end_headers()
            data =f"""
            <html>
                <head>
                    <title>Ola, mundo!</title>
                </head>
                <body>
                    <p> Testando servidor HTTP </p>
                    <p> Diretorio: {self.path}</p>
                </body>
            </html>            
            """.encode()
            self.wfile.write(data)

        elif self.path == "/eventos":
            self.send_response(200)
            self.send_header("Contet-Type", "text/html; charset=utf-8")
            self.end_headers()
            data =f"""
            <html>   
                <p> OI</p>
            </html>            
            """.encode()
            self.wfile.write(data)
            
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()