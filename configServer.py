import os
import random
import urllib.request

from globals import *

#Functions
#OS
def make_db_dir(db_dir):
    os.makedirs(db_dir,exist_ok=True)

#Network
def download_db(url, file_to):
    urllib.request.urlretrieve(url,file_to)

#IO
def extract(file_from, word_size):
    word_list = []
    try:
        with open(file_from, encoding="utf8") as input_file:
            for line in input_file:
                if len(line) ==  word_size + 1:
                    word_list.append(line)
    except:
        print("Can't open db")
        exit(1)
    return word_list

def save_random_list(word_list, file_to, up_to=100_000):
    random.shuffle(word_list)
    with open(file_to,'w', encoding='utf8') as output_file:
        for number,line in enumerate(word_list):
            if number >= up_to:
                break
            output_file.write(line)

#System
def main():
    #make_db_dir(db_folder)
    #download_db(url_all_words,db_all)
    words = extract(db_all, word_size)
    save_random_list(words, db_words, max_db_words)
    print(words)
    print("Done")

if __name__ == '__main__':
    main()
