import os
import sys
from cfwebscrape import cfwebscrape
from atwebscrape import atwebscrape

if(len(sys.argv) < 3):
    print("Usage : python generate_files.py {at/cf} {contest_link}")
    sys.exit(1)

SITE = sys.argv[1]
LINK = sys.argv[2]

if(SITE == 'at'):
    contest = atwebscrape(LINK)
elif(SITE == 'cf'):
    contest = cfwebscrape(LINK)

root_dir = contest.CONTEST_NAME
os.mkdir(root_dir)

questions = contest.QUESTION_NAMES

with open("template.cpp", "r") as f:
    template_content = f.read()

for quest in questions:

    file_name = os.path.join(root_dir, quest + ".cpp")

    with open(file_name, "w") as f:
        f.write(template_content)

testFolder_path = os.path.join(root_dir, "tests")
os.mkdir(testFolder_path)

for quest in questions:
    questTestFolder_path = os.path.join(testFolder_path, quest)
    os.mkdir(questTestFolder_path)

    inps, outs = contest.get_testCases(quest)

    for i in range(len(inps)):
        inp_file = os.path.join(questTestFolder_path, f"inp_{i + 1}.txt")
        out_file = os.path.join(questTestFolder_path, f"out_{i + 1}.txt")

        with open(inp_file, "w") as f:
            f.write(inps[i])
        
        with open(out_file, "w") as f:
            f.write(outs[i])

    