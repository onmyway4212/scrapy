import json
with open('top-stackoverflow-questions.json', 'r') as f:
    aa = json.load(f)                                   # 读文件+反序列化转化为字典

bb = json.dumps(aa, indent=4)
print(bb)

