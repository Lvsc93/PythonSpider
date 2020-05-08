import requests
import time
import tqdm
from bs4 import BeautifulSoup

def get_content(traget_chapter):
        req_chapter = requests.get(url = traget_chapter)
        req_chapter.encoding = 'utf-8'
        html_chapter = req_chapter.text
        bs = BeautifulSoup(html_chapter,'lxml')
        texts = bs.find('div',id = 'content')
        content_chapter = texts.text.strip().split('\xa0'*4)
        return content_chapter

if __name__ == '__main__':
    server = "https://www.xsbiquge.com/"
    book_name = "圣墟.txt"
    target = "https://www.xsbiquge.com/74_74821/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html,'lxml')
    chapters = chapter_bs.find('div',id = 'list').find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name,'a',encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')

