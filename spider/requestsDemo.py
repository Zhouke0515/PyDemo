import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException


def get():
    global response
    response = requests.get('https://www.httpbin.org/get')
    print(response.text)


def get_with_params():
    global response
    params = dict({
        'name': 'zk',
        'test': True
    })
    response = requests.get('https://www.httpbin.org/get', params=params)
    print(response.text)


def get_binary():
    global response
    response = requests.get('https://www.github.com/favicon.ico')
    print(response.text)
    print(response.content)

    with open('favicon.ico', 'wb') as f:
        f.write(response.content)


def get_exception():
    global response
    try:
        response = requests.get('http://www.baidu.com', timeout=0.01)
        print(response.status_code)
    except ReadTimeout:
        print('read timeout')
    except ConnectionError:
        print('connection timeout')
    except RequestException:
        print('request exception')


if __name__ == '__main__':
    get()
    get_with_params()
    get_binary()
    get_exception()
    pass
