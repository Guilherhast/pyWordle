import os

#Current directory
root_dir = os.path.realpath(os.path.dirname(__file__))

#db folder and files
db_folder = os.path.join(root_dir,'cfg')

db_all  = os.path.join(db_folder, 'db.txt')
db_words  = os.path.join(db_folder, 'words.txt')
db_start  = os.path.join(db_folder, 'time.txt')

#Server
port = 8000
hostname = '0.0.0.0'

server_cfg = (hostname,port)

public_folder = os.path.join(root_dir,"public")

api_re = '/api.*'
param_re = 'day=(\\d+)'

#Config
url_all_words = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'
word_size = 5
max_db_words = 30

#Print variables
if __name__ == '__main__':
    #Files
    print(root_dir)
    print(db_folder)
    print(db_all)
    print(db_words)
    print(db_start)
    #Server
    print(server_cfg)
    print(public_folder)
    print(api_re)
    print(param_re)
    #Config
    print(url_all_words)
    print(word_size)
    print(max_db_words)
