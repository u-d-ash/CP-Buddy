import requests
from bs4 import BeautifulSoup

class atwebscrape:

    def __init__(self, contest_link):
        self.CONTEST_LINK = contest_link
        self.CONTEST_NAME = contest_link.removeprefix("https://atcoder.jp/contests/")

        tasks_link = contest_link + "/tasks"
        html = requests.get(tasks_link).text
        soup = BeautifulSoup(html, 'lxml')

        #--- To get task names (A, B.. etc) ---

        table = soup.find('table', class_ = "table table-bordered table-striped")
        tbody = table.find('tbody')
        trs = tbody.find_all('tr')
        names = []
        for tr in trs:
            name = tr.find('a').text
            names.append(name)

        self.QUESTION_NAMES = names
    
    
    def get_testCases(self, ques):
        ques_link = self.CONTEST_LINK + "/tasks/" + self.CONTEST_NAME + "_" + ques.lower()

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
    