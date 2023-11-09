from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

import time
import warnings
import re
import random
import os

print("Start crawling...")
warnings.filterwarnings('ignore')

print("Setting Options...")
options = webdriver.ChromeOptions()
options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

webtoon_url = 'https://comic.naver.com/webtoon/list?titleId='
webtoon_titleId = [
    # '817081',
    # '783052',
    # '769209',
    # '747269',
    # '641253',
    # '792651',
    # '812354',
    # '783053',
    '717481',
    '796152'
]
webtoon_detailId = []

print("Setting Driver...")
for title_id in webtoon_titleId:
    driver.get(webtoon_url+title_id)
    time.sleep(1)

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    raw_count = soup.select_one(".EpisodeListView__count--fTMc5").text
    last_count = int(
        re.search("총 ([0-9]+)화", raw_count).group(1))

    start_count = last_count - 50 if (last_count >= 50) else 1
    webtoon_detailId.append([start_count + 1, last_count + 1])


def save_comment(title_id, start_count, last_count):
    print("Start Collecting: ", title_id)
    for detail_id in range(start_count, last_count):
        print(
            f"Open {title_id}: {detail_id-start_count+1} / {last_count-start_count}")

        detail_url = f'https://comic.naver.com/webtoon/detail?titleId={title_id}&no={detail_id}'
        driver.get(detail_url)
        time.sleep(1)

        print('Parcing comments.')
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        comments = soup.select(".u_cbox_contents")
        comments_text = []
        for comment in comments:
            comments_text.append(comment.text)
        print("Saving comments...")
        f = open(f'./data/{title_id}.txt', 'a')
        for comment in comments_text:
            f.write(comment+'\n')
        f.close()


for (idx, title_id) in enumerate(webtoon_titleId):
    start_count = webtoon_detailId[idx][0]
    last_count = webtoon_detailId[idx][1]
    save_comment(title_id, start_count, last_count)

print("Done.")
