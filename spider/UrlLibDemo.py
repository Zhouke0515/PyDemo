import urllib.parse
import urllib.request as request


def run():
    response = request.urlopen('http://www.baidu.com')
    print(response.read().decode('utf-8'))

    data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')
    response = request.urlopen('http://www.httpbin.org', data=data)
    print(response.read())


if __name__ == '__main__':
    run()
