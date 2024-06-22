import os
import sys
from contestac import contest_activity
from playwright.sync_api import sync_playwright
from config import *
from alive_progress import alive_bar

class contestmode:

    def __init__(self, SITE, LINK):

        self.site = SITE
        self.link = LINK
    
    def play(self):

        with alive_bar(total=None, bar = None, spinner = 'classic', elapsed = False, monitor = False, stats = False) as bar:

            contestActivity = contest_activity(self.site, self.link)

            playwright = sync_playwright().start()
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()

            logpage = context.new_page()

            if(self.site == 'cf'):
                logpage.goto('https://codeforces.com/enter?back=/')
                logpage.fill('[name="handleOrEmail"]', config_dict['CF_USERNAME'])
                logpage.fill('[name="password"]', config_dict['CF_PASSWORD'])
                logpage.click('[type="submit"]')
            elif(self.site == 'at'):
                logpage.goto('https://atcoder.jp/login?continue=https://atcoder.jp/')
                logpage.fill('[name="username"]', config_dict['AT_USERNAME'])
                logpage.fill('[name="password"]', config_dict['AT_PASSWORD'])
                logpage.click('[type="submit"]')

        print("Setup complete !")

        while True:
            command = input()
            command_split = command.split(" ")

            p_command = command_split[0]

            if(p_command == "open"):
                contestActivity.open_file(command_split[1])
            elif(p_command == "check"):
                contestActivity.check(command_split[1])
            elif(p_command == "submit"):
                contestActivity.submit(command_split[1], logpage)
            elif(p_command == "rank"):
                contestActivity.rank(command_split[1], logpage)
            elif(p_command == "exit"):
                sys.exit(1)
            elif(p_command == "clear"):
                os.system("clear")
            else:
                print("Enter valid command !\n")