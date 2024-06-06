import os
import sys
from problemac import problem_activity
from playwright.sync_api import sync_playwright
from config import config_dict

class practicemode:

    def play(self):

        problemActivity = problem_activity()

        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        cf_logpage = context.new_page()
        at_logpage = context.new_page()

        cf_logpage.goto('https://codeforces.com/enter?back=/')
        cf_logpage.fill('[name="handleOrEmail"]', config_dict['CF_USERNAME'])
        cf_logpage.fill('[name="password"]', config_dict['CF_PASSWORD'])
        cf_logpage.click('[type="submit"]')

        cf_logpage.wait_for_url('https://codeforces.com/')

        at_logpage.goto('https://atcoder.jp/login?continue=https://atcoder.jp/')
        at_logpage.fill('[name="username"]', config_dict['AT_USERNAME'])
        at_logpage.fill('[name="password"]', config_dict['AT_PASSWORD'])

        at_logpage.click('[type="submit"]')

        pages = [at_logpage, cf_logpage]

        print("Setup complete !")

        while True:

            #open cf 1931A
            #check at ABC340C

            command = input()
            command_split = command.split(" ")

            p_command = command_split[0]
            site = command_split[1]
            problem_id = command_split[2]

            if(p_command == "open"):
                #DONE
                problemActivity.open_file(site, problem_id)

            elif(p_command == "check"):
                #DONE
                problemActivity.check(site, problem_id)

            elif(p_command == "submit"):
                #DONE
                problemActivity.submit(site, problem_id, pages)

            elif(p_command == "exit"):
                sys.exit(1)
            elif(p_command == "clear"):
                os.system("clear")
            else:
                print("Enter valid command !\n")