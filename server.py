from http.server import BaseHTTPRequestHandler, HTTPServer

from globals import *

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        word = get_word(self.path)

        self.wfile.write(bytes(word, "utf-8"))

#Functions
#Calculation
def get_word(path=''):
    return 'Berro'

#System
def main():
    webServer = HTTPServer(server_cfg, Server)
    print("Server started http://%s:%s" % server_cfg)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

#Run
if __name__ == "__main__":
    main()
