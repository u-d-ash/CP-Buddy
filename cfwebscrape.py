import requests
from bs4 import BeautifulSoup

class cfwebscrape:

    def __init__(self, contest_link):

        self.CONTEST_LINK = contest_link
        self.CONTEST_NAME = "cf" + contest_link.removeprefix("https://codeforces.com/contest/")

        html = requests.get(contest_link).text

        soup = BeautifulSoup(html, 'lxml')

        #--- Getting the question names (A, B, ...)---

        table = soup.find_all('table', class_ = 'problems')
        trs = table[0].find_all('tr')

        questions = []

        for tr in trs:
            a = []
            for td in tr.find_all('td'):
                name = td.find('a').text
                name = "".join(line.strip() for line in name.split("\n"))
                a.append(name)
            
            if(len(a) >= 1):
                questions.append(a[0])
        
        self.QUESTION_NAMES = questions
    
    def get_testCases(self, ques):
        
        # ques = A, B... etc
        ques_link = self.CONTEST_LINK + "/problem/" + ques
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
                input_list.append(pre_tag.text)
            else:
                in_text = ""
                for div in sub_divs:
                    in_text += (div.text + "\n")
                input_list.append(in_text)
        
        for output_div in output_divs:
            output_list.append(output_div.find('pre').text)

        return input_list, output_list



