import requests
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import re
import time

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRkNTQzMGU3ZDM1NzNjZDZiYzAzZjhlYThlYTE2MGE4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUVOVHpPS1RJa3NxbGNPdU01dHp1Qjc1UUkzdnhPbWpGV3lQVkNIYWxwN289BjsARg%3D%3D--ee5172d622c5cf93b17255ecbe432f185bc493af; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1548318064,1548405723; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1548405723',
    'Host': 'www.xicidaili.com',
    'Upgrade-Insecure-Requests': '1',
}

def get_page(url):
    try:
        response = requests.get(url, headers=base_headers)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('访问失败', url)
        return None


def parse_page(html):
    if html:
        doc = pq(html)
        trs = doc('.clearfix.proxies table tr:gt(0)').items()
        """class=clearfix proxies"""
        for tr in trs:
            ip = tr.find('td:nth-child(1)').text()

            port = tr.find('td:nth-child(2)').text()

            yield ':'.join([ip, port])







def main(x):
    url_base ='https://www.xicidaili.com/nn/{}'
    for i in range(1,x):
        url=url_base.format(i)

        html = get_page(url)
        items = parse_page(html)







if __name__ == '__main__':
    x = 4
    main(x)





"""import requests,re
import time

def craw_66ip():
    url = 'http://www.66ip.cn/{}.html'
    for i in range(1, 3):
        url1=url.format(i)
        r = requests.get(url1)
        print('抓取成功', url1, r.status_code)
        time.sleep(4)
"""











