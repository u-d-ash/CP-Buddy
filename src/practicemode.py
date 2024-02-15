from imports import *

class practicemode:

    def __init__(self, SITE):

        self.site = SITE
    
    def play(self):

        print("Setup complete !")

        while True:

            #open cf 1931A
            #check at ABC340C

            command = input()
            command_split = command.split(" ")

            p_command = command_split[0]
            site = command_split[1]
            problem_id = command_split[2]

            problemActivity = problem_activity()

            if(p_command == "open"):

                problemActivity.open_file(site, problem_id)

            elif(p_command == "check"):

                problemActivity.check(site, problem_id)

            elif(p_command == "submit"):

                print("Implement Submit for Practice Mode")

            elif(p_command == "exit"):
                sys.exit(1)
            elif(p_command == "clear"):
                os.system("clear")
            else:
                print("Enter valid command !\n")