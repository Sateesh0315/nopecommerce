import os


file_path = os.path.dirname(os.path.abspath(__file__))
for subdirs in os.walk(os.getcwd()):
    print(subdirs)