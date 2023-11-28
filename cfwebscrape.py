import requests
from bs4 import BeautifulSoup

def get_queslist(CONTEST_LINK):

    html_text = requests.get(CONTEST_LINK).text
    html_text = "".join(line.strip() for line in html_text.split("\n"))
    soup = BeautifulSoup(html_text, 'lxml')
        
    table = soup.find_all('table', class_ = 'problems')
    trs = table[0].find_all('tr')

    Questions = []

    for i, tr in enumerate(trs):
        luls = []
        for j, td in enumerate(trs[i].find_all('td')):
            luls.append(td.find('a').text)
        
        if(len(luls) >= 1):
            Questions.append(luls[0] + ".cpp")
    
    return Questions

def get_contestname(CONTEST_LINK):

    return CONTEST_LINK.removeprefix("https://codeforces.com/contest/")





