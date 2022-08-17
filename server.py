import re
import functools
import linecache

from datetime import datetime
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
    #Read day values
    n_ans = 1
    n_path = get_day_from_path(param_re,path)
    n_cfg = get_day_from_cfg(db_start)
    #Fix numbers
    if n_path>0:
        n_ans = min(n_path,n_cfg)
    else:
        n_ans = n_cfg

    word = get_nth_word(db_words,n_ans)
    word = word[:-1]
    return word

def get_day_from_path(regex, path = ''):
    day = 0
    search = re.search(regex, path)
    if search:
        day_str = search.group(1)
        day = int(day_str)
    return day

def get_day_from_cfg(file_from):
    start = get_start_date(file_from)
    now = datetime.today()

    delta = now - start

    return delta.days + 1


#IO
def get_start_date(file_from):
    date_str = linecache.getline(file_from,1)
    date_str = date_str[:-1]
    day = datetime.fromisoformat(date_str)
    return day

def get_nth_word(file_from,n=1):
    return linecache.getline(file_from,n)

#System
def main():
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
