## CPBuddy

Competitive programming is a sport where your minutes matter a ton. Switching screens and tabs, copy pasting your code, waiting for the "AC" verdict while keeping an eye on your competitors is a pain in the ***. We are not GPUs.

Enter CP-Buddy.

* Create a dedicated contest-directory
* Check Sample Test Cases
* Submit Code
* Get Contest Ranks of your Friends

**RIGHT FROM YOUR TERMINAL WINDOW !!!**

---

### Usage

#### Installation & Setup

1. Clone the repository and install the requirements
 `pip install requirements.txt`
2. Setup the `config.py` file
    * Add the login credintials in the `CONFIG_DICT`
    * Add the path to your directory where all your files will go in `ROOTFOLDER`

#### Features

**Contest Mode**
* Use as : `python main.py c {site} {contest-link}`
    * site : either of `['cf, 'at']` for codeforces and atcoder respectively
    * contest-link : link of the contest
* MAKE SURE YOU RUN THE COMMAND AFTER THE CONTEST BEGINS, NOT BEFORE !

Commands:
1. `open A` : open the code file for problem A
2. `check A` : check problem A against sample test cases
3. `submit A` : make the submission for problem A
4. `rank {user}` : get the rank of the user
5. `clear` : to clear the terminal screen
5. `exit` : to terminate the program

**Practice Mode**
* Use as : `python main.py p`

Commands:
1. `open {site} {problem-id}`
    * site : either of ['cf', 'at']
    * problem-id : examples : 1934a (codeforces), abc356a (atcoder)
2. `check {site} {problem-id}`
3. `submit {site} {problem-id}`

> It's still in a "beta" stage. *"lmao"*. Personally I haven't used it a lot and it's being continuously developed.

---