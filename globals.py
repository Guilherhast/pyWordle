import os

#Current directory
root_dir = os.path.realpath(os.path.dirname(__file__))

#db folder and files
db_folder = os.path.join(root_dir,'cfg')

db_all  = os.path.join(db_folder, 'db.txt')
db_words  = os.path.join(db_folder, 'words.txt')
db_start  = os.path.join(db_folder, 'time.txt')

#Print variables
if __name__ == '__main__':
    #Files
    print(root_dir)
    print(db_folder)
    print(db_all)
    print(db_words)
    print(db_start)
