from imports import *

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
    
    #---- SUBMIT FUNCTIONS (TO BE ADDED) ----
        
        
    def cf_submit(self, ques):

        print("cfsubmit")
    
    def at_submit(self, ques):

        print("atsubmit")

    
    def submit(self, ques):
    
        if(self.SITE == 'cf'):
            self.cf_submit(ques)
        elif(self.SITE == 'at'):
            self.at_submit(ques)


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