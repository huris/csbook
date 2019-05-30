#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这是一个爬虫计算机书籍的程序
import json
import re
import requests
import random


def get_headers():
    '''
    随机获取一个headers
    '''
    user_agents = ['Mozilla/5.0(Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0(Windows; U; Windows NT 6.1; en-us)AppleWebKit/534.50(KHTML, likeGecko)Version/5.1Safari/534.50',
                   'Opera/9.80(Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                   'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                   'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
                   'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
                   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
                   'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
                   'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
                   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
                   'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                   'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
                   'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
                   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
                   'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
                   'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
                   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
                   'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
                   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
                   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
                   'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
                   'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                   'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.1'
                   ]
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


if __name__ == '__main__':
    fenlei = [
        'web-development',
        'programming',
        'datebases',
        'graphics-design',
        'operating-systems',
        'networking-cloud-computing',
        'administration',
        'certification',
        'computers-technology',
        'enterprise',
        'game-programming',
        'hardware',
        'marketing-seo',
        'security',
        'software']
    base_url = 'http://www.allitebooks.com/'
    book_link_pattern = 'href="(.*)" rel="bookmark">'
    down_link_pattern = 'href="(http:\/\/file.*.pdf)" target="_blank">'
    down_link_pattern1 = 'href="(http:\/\/file.*.epub)" target="_blank">'

    url = 'http://www.allitebooks.org/big-data-analytics/'
    url2 = 'http://www.allitebooks.org/phoenix-in-action/'

    pos = [
        'name', 'author', 'ISBN',
        'year', 'pages', 'language',
        'category', 'picture', 'description',
        'download_link_pdf', 'download_link_epub',
        'price'
    ]

    for classification in fenlei:
        print(classification)
        f = open(classification + '.json', 'a')
        new_url = base_url + classification + '/page/{}'
        req = requests.get(new_url.format(1), headers=get_headers()).text
        pagenum = re.search('<span class="pages">1 / (.*) Pages</span>', req).group()[24:-13]
        for i in range(int(pagenum)):
            req = requests.get(new_url.format(1), headers=get_headers()).text
            book_link = re.findall(book_link_pattern, req)
            book_link = list(set(book_link))
            for url in book_link:
                req = requests.get(url, headers=get_headers()).text
                # print(req)
                dic = {}
                try:
                    dic['name'] = re.findall("<h1 class=\"single-title\">(.*)</h1>", req)[0]
                    dic['author'] = re.findall("<dt>Author:</dt><dd> <a href=\".*\" rel=\"tag\">(.*)</a></dd>", req)[0]
                    dic['ISBN'] = re.findall("<dt>ISBN-10:</dt><dd> (.*)</dd>", req)[0]
                    dic['year'] = re.findall("<dt>Year:</dt><dd> (.*)</dd>", req)[0]
                    dic['pages'] = int(re.findall("<dt>Pages:</dt><dd> (.*)</dd>", req)[0])
                    dic['language'] = re.findall("<dt>Language:</dt><dd> (.*)</dd>", req)[0]
                    dic['category'] = \
                        re.findall("<dt>Category:</dt><dd> <a href=\".*\" rel=\"category\" >(.*)</a></dd>", req)[0]
                    dic['language'] = re.findall("<dt>Language:</dt><dd> (.*)</dd>", req)[0]
                    dic['picture'] = re.findall("<img width=\".*\" height=\".*\" src=\"(.*?)\"", req)[0]
                    str = \
                        re.findall("<div class=\"entry-content\">(.*)<!-- END \.entry-content -->", req,
                                   flags=re.DOTALL)[
                            0]
                    str = re.sub(r" +", " ", str)
                    str = re.sub(r"<[hp]\d?>", "", str)
                    str = re.sub(r"</[hp]\d?>", "", str)
                    str = re.sub(r"&#\d{4};", " ", str)
                    str = re.sub(r"</div>", "", str)
                    str = re.sub(r"</*ul>", "", str)
                    str = re.sub(r"</*li>", "", str)
                    dic['description'] = str
                    try:
                        dic['download_link_pdf'] = re.search(down_link_pattern, req).group()[6:-18]
                        dic['download_link_epub'] = re.search(down_link_pattern1, req).group()[6:-18]
                    except:
                        try:
                            dic['download_link_pdf'] = re.search(down_link_pattern, req).group()[6:-18]
                            dic['download_link_epub'] = None
                        except:
                            try:
                                dic['download_link_pdf'] = None
                                dic['download_link_epub'] = re.search(down_link_pattern1, req).group()[6:-18]
                            except:
                                dic['download_link_pdf'] = None
                                dic['download_link_epub'] = None
                                pass
                    dic['price'] = random.randint(30, 200)
                    # dicarray.append(dic)
                    f.write(json.dumps(dic))
                    f.write(',')
                    f.write('\n')
                    # print(now)
                    # now += 1
                except:
                    print(req)
        f.close()
