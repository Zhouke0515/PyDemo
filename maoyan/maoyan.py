import json
import logging
import os
import re
from multiprocessing import Pool

import requests
from requests.exceptions import RequestException

HOST = 'http://www.maoyan.com'
PATH = '/board/4'


def get_one_page(url):
    r'''
    请求URL

    :param url: 请求的URL
    :return: 响应的内容
    '''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    response = None
    try:
        response = requests.get(url, headers=headers)
    except RequestException:
        print()
    if (response.status_code == 200):
        logging.log(logging.INFO, '请求URL成功')
        return response.text
    else:
        return None


def parse_content(html):
    r'''
    解析爬取的内容

    :param html: 响应的内容
    :return: 解析后的结果{排名，电影名，主演，上映日期}
    '''
    pattern = re.compile(r'<dd.*?board-index.*?>(\d{1,3})</i>'
                         r'.*?movie-item-info.*?'
                         r'<p.*?name.*?<a.*?>(.*?)</a></p>.*?'
                         r'<p.*?"star".*?>(.*?)</p>.*?'
                         r'<p.*?"releasetime".*?>(.*?)</p>.*?'
                         r'</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'rank': item[0],
            'name': item[1],
            'stars': item[2].strip(),
            'time': item[3].strip()[5:]
        }
    return items


def generate_url(offset):
    r'''
    生成url

    :param offset: URL参数offset的值[0,10,20,30,40,50,60,70,80,90]
    :return: 生成的URL
    '''
    if not isinstance(offset, int):
        raise TypeError('必须是整数类型')
    params = set()
    for param in range(0, 100, 10):
        params.add(param)
    if offset not in params:
        raise ValueError('parameter值错误,值列表', params)
    url = HOST + PATH + '?offset=' + str(offset)
    logging.log(logging.INFO, '生成URL成功')
    return url


def save_to_file(content):
    r'''
    写入数据到文件
    :param content:
    :return:
    '''
    dir_path = os.path.join(os.path.abspath('.'), 'maoyan')
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    file_path = os.path.join(dir_path, 'maoyan_top100.txt')
    # print('文件路径：', file_path)
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            data = json.dumps(content, ensure_ascii=False) + '\n'
            f.write(data)
            f.close()
    except Exception:
        print('写入文件失败')


def main(offset):
    r'''

    :param offset:
    :return:
    '''
    # for offset in range(0, 100, 10):
    url = generate_url(offset)
    html = get_one_page(url)
    result = parse_content(html)
    for i in result:
        print(i)
        save_to_file(i)


if __name__ == '__main__':
    # 使用进程池
    pool = Pool()
    pool.map(main, range(0, 100, 10))

