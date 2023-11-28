import cfwebscrape
import atwebscrape
import os
import sys

#usage : python generate_files.py {at/cf} {contest link}
if(len(sys.argv) < 3):
    print("Usage: python generate_files.py {at/cf} {contest link}")
    sys.exit(1)

SITE = sys.argv[1]
LINK = sys.argv[2]

if(SITE == 'at'):
    questions = atwebscrape.get_queslist(LINK)
    contest_name = atwebscrape.get_contestname(LINK)
elif(SITE == 'cf'):
    questions = cfwebscrape.get_queslist(LINK)
    contest_name = cfwebscrape.get_contestname(LINK)

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
