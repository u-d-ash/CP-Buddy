import cfwebscrape
import os

questions = cfwebscrape.get_queslist()
contest_name = cfwebscrape.get_contestname()

try:
    os.mkdir(contest_name)
except FileExistsError:
    print("Folder already exists !!")

try:
    with open("template.cpp", 'r') as source_file:
        file_content = source_file.read()
except FileNotFoundError:
    print("Template file not found")

for file_name in questions:
    file_path = os.path.join(contest_name, file_name)
    with open(file_path, 'w') as file:
        file.write(file_content)
