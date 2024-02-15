from imports import *

def main():
    # usage (contest mode): 
    # -> python main.py cf c https://codeforces.com/contest/1907

    # usage (practice mode)
    # -> python main.py cf p

    # more debugging checks to be added

    if(len(sys.argv) == 2):

        SITE = sys.argv[1]

        practicemode(SITE).play()

    elif(len(sys.argv) == 3):

        SITE = sys.argv[1]
        LINK = sys.argv[3]

        contestmode(SITE, LINK).play()


if __name__ == "__main__":
    main()


