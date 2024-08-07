
from bs4 import BeautifulSoup
from urllib.request import urlopen

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comong_project.settings")
import django
django.setup()

from Community.models import Notice
base = "https://ko.hongik.ac.kr"
url = "https://ko.hongik.ac.kr/front/boardlist.do?bbsConfigFK=54&siteGubun=1&menuGubun=1"

def parser():
    html = urlopen(url)
    data={}
    obj = BeautifulSoup(html,"html.parser")
    notice = obj.select('body > div > div > div:nth-child(3) > div > table > tbody > tr> td> div  ')
    for title in notice:
        data[title.getText().strip()]=title.find("a")["href"]
    return data

notices = parser()
# Notice.objects.all().delete()

for t,l in notices.items():
    try :
        notice=Notice.objects.get(title = t)
    except Notice.DoesNotExist:
        Notice(title=t,content_url= base +l).save()
    
    