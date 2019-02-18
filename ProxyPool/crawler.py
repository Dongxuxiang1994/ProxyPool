import re
from pyquery import PyQuery as pq
from spider import get_page

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs,):
        count = 0
        attrs['__CrawlFunc__'] = []
        attrs['__CrawlName__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlName__'].append(k)
                attrs['__CrawlFunc__'].append(v)
                count += 1

        for k in attrs['__CrawlName__']:
            attrs.pop(k)
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        print('Site', callback)
        for func in self.__CrawlFunc__:
            if func.__name__ == callback:
                this_page_proxies = func(self)
                for proxy in this_page_proxies:
                    print('getting', proxy, 'from', callback)
                    proxies.append(proxy)
        print(proxies)
        return proxies


    def crawl_ip3366(self):
        for page in range(1, 20):
            start_url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            html = get_page(start_url)
            ip_adress = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
            # \s * 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(html)
            for adress, port in re_ip_adress:
                yield ':'.join([adress, port])
    #西刺爬了太多，反扒了
    """def crawl_xici(self):
        for i in range(1, 3):
            start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRkNTQzMGU3ZDM1NzNjZDZiYzAzZjhlYThlYTE2MGE4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUVOVHpPS1RJa3NxbGNPdU01dHp1Qjc1UUkzdnhPbWpGV3lQVkNIYWxwN289BjsARg%3D%3D--ee5172d622c5cf93b17255ecbe432f185bc493af; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1548318064,1548405723; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1548405723',
                'Host': 'www.xicidaili.com',
                'Upgrade-Insecure-Requests': '1',
            }
            html = get_page(start_url, options=headers)
            if html:
                doc = pq(html)
                trs = doc('.clearfix.proxies table tr:gt(0)').items()
                #class=clearfix proxies
                for tr in trs:
                    ip = tr.find('td:nth-child(2)').text()
                    port = tr.find('td:nth-child(3)').text()
                    yield ':'.join([ip, port])"""











