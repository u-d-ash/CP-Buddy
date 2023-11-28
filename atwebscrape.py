import requests
from bs4 import BeautifulSoup

def get_contestname(CONTEST_LINK):
    return CONTEST_LINK.removeprefix("https://atcoder.jp/contests/")

def get_queslist(CONTEST_LINK):

    QUESTIONS_LINK = CONTEST_LINK + "/tasks"
    html_text = requests.get(QUESTIONS_LINK).text
    html_text = "".join(line.strip() for line in html_text.split("\n"))
    soup = BeautifulSoup(html_text, 'lxml')

    table = soup.find('table', class_ = "table table-bordered table-striped")
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    names = []
    for tr in trs:
        name = tr.find('a').text
        names.append(name + ".cpp")
        
    return names

    print(names)