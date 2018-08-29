import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

person1 = {
    'name': '六所',
    'age': 34,
    'sex': 'M',
}


person2 = {
    'name': '李雷',
    'age': 32,
    'sex': 'M',
}


person3 = {
    'name': '韩梅梅',
    'age': 31,
    'sex': 'F',
}

r.hmset('person:1', person1)
r.hmset('person:2', person2)
r.hmset('person3', person3)

r.connection_pool.disconnect()

