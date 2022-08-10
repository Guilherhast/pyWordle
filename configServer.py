import os

from globals import *

#Functions
#OS
def make_db_dir(db_dir):
    os.makedirs(db_dir,exist_ok=True)

#System
def main():
    make_db_dir(db_folder)

if __name__ == '__main__':
    main()
