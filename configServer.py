import os
import urllib.request

from globals import *

#Functions
#OS
def make_db_dir(db_dir):
    os.makedirs(db_dir,exist_ok=True)

#Network
def download_db(url, file_to):
    urllib.request.urlretrieve(url,file_to)

#System
def main():
    #make_db_dir(db_folder)
    download_db(url_all_words,db_all)
    print("Done")

if __name__ == '__main__':
    main()
