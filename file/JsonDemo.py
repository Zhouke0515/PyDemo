import json
import os

d = dict(name='zk', age=27)
dir = os.path.join(os.path.abspath('.'), 'testdir')
fp = open(os.path.join(dir, 'test.txt'), 'w')
# dump 序列化json到文件
json.dump(d, fp)
# dumps 返回json字符串
print(json.dumps(d))

fp = open(os.path.join(dir, 'test.txt'), 'r')
print(json.load(fp))
print(json.loads(json.dumps(d)))
