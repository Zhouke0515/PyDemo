import re

if __name__ == '__main__':
    content = r'asdaslkjdasd65a4s564asd45'
    pattern = re.compile('(\d)', re.S)
    result = re.findall(pattern, content)
    print(result)
