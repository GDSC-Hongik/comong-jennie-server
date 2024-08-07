
from bs4 import BeautifulSoup
from urllib.request import urlopen

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comong_project.settings")
import django
django.setup()

from Community.models import Notice

def parser():
    url = "https://ko.hongik.ac.kr/front/boardlist.do?bbsConfigFK=54&siteGubun=1&menuGubun=1"

    html = urlopen(url)
    data={}
    obj = BeautifulSoup(html,"html.parser")
    notice = obj.select('body > div > div > div:nth-child(3) > div > table > tbody > tr> td> div  ')
    for title in notice:
        data[title.getText()]=title.find("a")["href"]
    return data

notices = parser()
for t,l in notices.items():
    Notice(title=t,content_url=l).save()
    