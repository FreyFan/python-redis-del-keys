import redis

def del_hkeys(pattern) : 
cnt = redis.Redis(host=’xxxx’,port=6379,db=0) 
key_dict={} 
keys = cnt.keys(pattern); 
for key in keys: 
subkeys = cnt.hkeys(key) 
key_dict[key] = subkeys 
for key in key_dict.keys(): 
subkeys = key_dict[key]

    for subkey in subkeys:
        if str(subkey).__contains__("http://report"):
            print subkey
            cnt.hdel(key, subkey)
del_hkeys(“crawler_distinct_redis_setname”)