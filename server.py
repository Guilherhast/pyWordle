import re
import functools

from http.server import SimpleHTTPRequestHandler, HTTPServer

from globals import *

class Server(SimpleHTTPRequestHandler):
    def do_GET(self):
        if re.match(api_re,self.path):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()

            word = get_word(self.path)

            self.wfile.write(bytes(word, "utf-8"))
        else:
            SimpleHTTPRequestHandler.do_GET(self)

#Functions
#Calculation
def get_word(path=''):
    return 'Berro'

#System
def main():
    word = get_word()
    print(word)

def main_():
    handler = functools.partial(Server,directory=public_folder)
    webServer = HTTPServer(server_cfg, handler)
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
