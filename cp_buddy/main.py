import sys
from cp_buddy.contestmode import contestmode
from cp_buddy.practicemode import practicemode
from cp_buddy.config import *

def main():
    # usage (contest mode): 
    # -> python main.py c cf https://codeforces.com/contest/1907

    # usage (practice mode)
    # -> python main.py p

    # more debugging checks to be added
    
    if(len(sys.argv) == 2):

        practicemode().play()

    elif(len(sys.argv) == 4):

        SITE = sys.argv[2]
        LINK = sys.argv[3]

        contestmode(SITE, LINK).play()


if __name__ == "__main__":
    main()


