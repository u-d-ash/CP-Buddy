import requests
from bs4 import BeautifulSoup

LINK = "https://codeforces.com/contest/1900"

html_text = requests.get(LINK).text
html_text = "".join(line.strip() for line in html_text.split("\n"))
soup = BeautifulSoup(html_text, 'lxml')

def get_queslist():
    
    table = soup.find_all('table', class_ = 'problems')
    trs = table[0].find_all('tr')

    Questions = []

    for i, tr in enumerate(trs):
        luls = []
        for j, td in enumerate(trs[i].find_all('td')):
            luls.append(td.find_all('a')[0].text)
        
        if(len(luls) >= 1):
            Questions.append(luls[0] + ".cpp")
    
    return Questions

def get_contestname():

    sb = soup.find_all('div', id = "sidebar")
    box = sb[0].find('table', class_ = "rtable")
    return box.find_all('a')[0].text





