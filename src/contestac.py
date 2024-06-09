import os
import subprocess
from atwebscrape import atwebscrape
from cfwebscrape import cfwebscrape
from config import config_dict
from playwright.sync_api import sync_playwright
import sys
import requests
import json
from bs4 import BeautifulSoup

def equality(stdout, output):
        
    std = stdout.split("\n")
    out = output.split("\n")

    clean_std = []
    clean_out = []

    for s in std:
        if(s != ''):
            clean_std.append(s)
    
    for o in out:
        if(o != ''):
            clean_out.append(o)

    if(len(clean_std) != len(clean_out)):
        return False

    for i in range(len(clean_out)):
        if(clean_out[i] != clean_std[i]):
            return False
    
    return True

class contest_activity:

    def __init__(self, site, link):
        self.SITE = site
        self.LINK = link

        if(site == 'at'):
            self.CONTEST = atwebscrape(link)

        elif(site == 'cf'):
            self.CONTEST = cfwebscrape(link)
        
        # Generating working directory

        root_dir = self.CONTEST.CONTEST_NAME
        os.mkdir(root_dir)

        questions = self.CONTEST.QUESTION_NAMES

        with open("template.cpp", "r") as f:
            template_content = f.read()

        for quest in questions:

            file_name = os.path.join(root_dir, quest + ".cpp")

            with open(file_name, "w") as f:
                f.write(template_content)
        
    def open_file(self, ques):
 
        os.system(f"code {self.CONTEST.CONTEST_NAME}/{ques}.cpp")
     
    def submit(self, ques, page):
    
        if(self.SITE == 'cf'):
            
            file_name = ques + ".cpp"

            file_path = f"{sys.path[0]}/{self.CONTEST.CONTEST_NAME}/{file_name}"

            cont_id = self.CONTEST.CONTEST_NAME[2:]

            page.goto(f'https://codeforces.com/contest/{cont_id}/submit')

            list_index = ord(ques) - ord('A') + 1

            page.locator('[name="submittedProblemIndex"]').select_option(index = list_index)

            page.locator('[name="programTypeId"]').select_option(label = "GNU G++17 7.3.0")

            with page.expect_file_chooser() as fc_info:
                page.click('[name="sourceFile"]')

            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            page.click('[value = "Submit"]')

            ## TODO : ADD SOME SORT OF LOADING WIDGET HERE !!!

            ver = "TESTING"

            while(ver == "TESTING"):
                response = requests.get(f"https://codeforces.com/api/user.status?handle={config_dict['CF_USERNAME']}&from=1&count=1")
                json_dict = json.loads(response.text)

                stat = json_dict["status"]

                if(stat != "OK"):
                    continue
                
                ver = json_dict["result"][0]["verdict"]
            
            if(ver == "OK"):

                print("ACCEPTED !!!")
            
            else:

                print(ver)

        elif(self.SITE == 'at'):

            file_path = f"{sys.path[0]}/{self.CONTEST.CONTEST_NAME}/{file_name}"

            page.goto(f"https://atcoder.jp/contests/{self.CONTEST.CONTEST_NAME}/tasks/{self.CONTEST.CONTEST_NAME}_{ques.lower()}")

            page.locator("[name='data.LanguageId']").select_option("C++ 17 (gcc 12.2)")

            with page.expect_file_chooser() as fc_info:
                page.click('[id="btn-open-file"]')

            file_chooser = fc_info.value
            file_chooser.set_files(file_path)

            page.click('[id="submit"]')

            verds = ['CE', 'IE', 'MLE', 'OLE', 'QLE', 'RE', 'TLE', 'WA', 'WR', 'AC']

            verdict = None

            while(verdict not in verds):

                page.goto(f"https://atcoder.jp/contests/{self.CONTEST.CONTEST_NAME}/submissions/me")

                cont = page.content()
                soup = BeautifulSoup(cont, 'lxml')
                table = soup.find('table')
                tbod = table.find('tbody')
                ross = tbod.find_all('tr')
                verdict = ross[0].find_all('td')[6].text
            
            if(verdict == 'AC'):
                print("ACCEPTED !!!")
            elif(verdict == 'TLE'):
                print("TIME LIMIT EXCEEDED !!!")
            elif(verdict == 'WA'):
                print("WRONG ANSWER !!!")
            elif(verdict == 'MLE'):
                print("MEMORY LIMIT EXCEEDED !!!")
            else:
                print(verdict)
           
    def check(self, ques):

        inps, outs = self.CONTEST.get_testCases(ques)
        script = ques + ".cpp"
        passed = []
        act_outs = []
        for i in range(len(inps)):
            command = f'g++ {self.CONTEST.CONTEST_NAME}/{script} -o {script[:-4]} && ./{script[:-4]}'
            process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin = subprocess.PIPE, shell=True, text = True)
            stdout = process.communicate(input=inps[i])[0]
            act_outs.append(stdout)
            passed.append(equality(stdout, outs[i]))
        
        for i in range(len(passed)):

            if(passed[i]):
                print(f"Sample Test Case {i + 1}/{len(passed)} Passed !")
            else:
                print(f"Sample Test Case {i + 1}/{len(passed)} Failed !")
                print("Your output : ")
                print(act_outs[i])
                print("Actual output : ")
                print(outs[i])

    def rank(self, username, page):

        if(self.SITE == 'cf'):
            cont_id = self.CONTEST.CONTEST_NAME[2:]

            stat = "NOTOK"

            while(stat != "OK"):

                response = requests.get(f"https://codeforces.com/api/contest.standings?contestId={cont_id}&handles={username}")
                resp_dict = json.loads(response.text)

                stat = resp_dict["status"]
            
            if(len(resp_dict["result"]["rows"]) == 0):
                print(f"{username} is not participating in the contest")
                return
            

            rank = resp_dict["result"]["rows"][0]["rank"]
            points = resp_dict["result"]["rows"][0]["points"]
            penalty = resp_dict["result"]["rows"][0]["penalty"]

            print(f"{username} is at rank {rank} with {points} points and {penalty} in penalties")
        else:

            page.goto(f"https://atcoder.jp/contests/{self.CONTEST.CONTEST_NAME}/standings")

            page.locator('span:has-text("Customize")').click()

            text_box = page.locator('[id="input-user"]')
            text_box.fill(username)
            ranks = page.locator('[class="standings-rank small80"]')
            text = ranks.text_content()
            rank = text.split(' ')[1][1:-1]

            print(rank)

        




        