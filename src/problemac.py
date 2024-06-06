import os
import sys
import subprocess
from playwright.sync_api import sync_playwright
import requests
from config import *
from bs4 import BeautifulSoup
import json

# For check function
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

# Scrapes the question page
def TCScraper(site, ques):

    if(site == 'at'):

        contestcode = ques[:-1].lower()
        quescode = ques[-1].lower()

        ques_link = f"https://atcoder.jp/contests/{contestcode}/tasks/{contestcode}_{quescode}"

        html = requests.get(ques_link).text
        soup = BeautifulSoup(html, 'lxml')

        the_divs = soup.find_all('div', class_ = "part")
        tcs = []
        for div in the_divs:

            h3_text = div.find('h3').text
            if("Sample" in h3_text):
                final_text = div.find('pre').get_text().rstrip()
                final_text = final_text.replace('\r', '')
                tcs.append(final_text)
        
        input_list = []
        output_list = []

        for i in range(len(tcs)):
            if(i % 2 == 0):
                input_list.append(tcs[i])
            else:
                output_list.append(tcs[i])
        
        return input_list, output_list

    elif(site == 'cf'):

        contestno = ques[:-1]
        quescode = ques[-1].upper()

        ques_link = f"https://codeforces.com/contest/{contestno}/problem/{quescode}"

        html = requests.get(ques_link).text
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_ = 'sample-test')
        input_divs = div.find_all('div', class_ = 'input')
        output_divs = div.find_all('div', class_ = 'output')
        
        input_list = []
        output_list = []

        for input_div in input_divs:
            pre_tag = input_div.find('pre')
            sub_divs = pre_tag.find_all('div')

            if(len(sub_divs) == 0):
                input = ""
                i = 0
                if(len(pre_tag.findAll('br')) != 0):
                    for lol in pre_tag.findAll('br'):
                        next_s = lol.previousSibling
                        input += str(next_s).strip()
                        if(i != len(pre_tag.findAll('br')) - 1):
                            input += "\n"
                        i += 1
                    input_list.append(input)
                else:
                    for pt in pre_tag:
                        input_list.append(pt.text[1:-1])
            else:
                in_text = ""
                i = 0
                for div in sub_divs:
                    if(i == len(sub_divs) - 1):
                        in_text += (div.text)
                    else:
                        in_text += (div.text + "\n")
                    i += 1
                
                input_list.append(in_text)

        for output_div in output_divs:
            output = ""
            outpre_tag = output_div.find('pre')

            if(len(outpre_tag.findAll('br')) == 0):
                final_text = outpre_tag.text.lstrip()
                final_text = final_text.rstrip()
                output_list.append(final_text)
            else:
                i = 0
                for lol in outpre_tag.findAll('br'):
                    next_s = lol.previousSibling
                    output += str(next_s).strip()
                    if(i != len(outpre_tag.findAll('br')) - 1):
                        output += "\n"
                    i += 1
                output_list.append(output)
            
        return input_list, output_list


class problem_activity:

    def __init__(self):
        self.FILE_LIST = []

    def open_file(self, site, ques):

        file_name = site + "_" + ques + ".cpp"

        if(file_name in self.FILE_LIST):

            os.system(f"code {file_name}")
        
        else:

            with open("template.cpp", "r") as f:
                template_content = f.read()
        
            with open(file_name, "w") as f:
                f.write(template_content)
    
            os.system(f"code {file_name}")

            self.FILE_LIST.append(file_name)

    def submit(self, site, ques, pages):

        if(site == 'cf'):

            file_name = site + "_" + ques + ".cpp"

            file_path = f"{sys.path[0]}/{file_name}"

            pages[1].goto('https://codeforces.com/problemset/submit')

            pages[1].fill('[name="submittedProblemCode"]', ques)
            with pages[1].expect_file_chooser() as fc_info:
                pages[1].click('[name="sourceFile"]')

            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            pages[1].click('[type="submit"]')

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


    def check(self, site, ques):

        inps, outs = TCScraper(site, ques)
        script = site + "_" + ques + ".cpp"
        passed = []
        act_outs = []
        for i in range(len(inps)):
            command = f'g++ {script} -o {script[:-4]} && ./{script[:-4]}'
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
