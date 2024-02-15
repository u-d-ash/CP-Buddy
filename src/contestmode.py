from imports import *

class contestmode:

    def __init__(self, SITE, LINK):

        self.site = SITE
        self.link = LINK
    
    def play(self):

        contestActivity = contest_activity(self.site, self.link)

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

                contestActivity.submit(command_split[1])
                
            elif(p_command == "rank"):
                #lmao
                print("rank")
            elif(p_command == "myrank"):
                #lmao
                print("lol")
            elif(p_command == "exit"):
                sys.exit(1)
            elif(p_command == "clear"):
                os.system("clear")
            else:
                print("Enter valid command !\n")