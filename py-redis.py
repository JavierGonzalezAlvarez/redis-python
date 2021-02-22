#name=key

def strings_redis():
    import redis
    #charset="utf-8", decode_responses=True => avoid b' in redis python
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)    
    print("-------------")
    print("STRINGS")
    print("-------------")

    #info()
    print(redis.info())
    print("-------------")
    
    #monitor()
    print(redis.monitor())
    print("-------------")
    
    #set()
    redis.set("name","javier")    
    redis.set("name","jaime")  
    print("key: ", redis.get("name"))  
    print("-------------")
    print("all keys: ", redis.keys())  
    print("keys with a 'name...': ", redis.keys("name*"))  
    print("keys with a 'e': ", redis.keys("*e*"))  
    print("-------------")

    #setnx(name, value)
    redis.set("name","javier")    

    #mset(name, value)
    redis.mset({"name": "peter", "name": "david"})    
    print("name: ", redis.mget("name"))         
    print("-------------")

    #getrange(name, start, end) - substrings of the value
    print("range : ", redis.getrange("name", 0, 3))


    #delete all keys     
    for key in redis.scan_iter("prefix:*"):
        redis.delete(key)

   
def hashes_redis():
    import redis    
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("HASH")
    print("-------------")

    #hmset(name, mapping) hget(name, key) hgetall(name)
    redis.hmset("user.1", {"name": "peter", "email": "siuuds@gmail.com"})    
    print("map.1: ", redis.hgetall("user.1"))    
    print("name.1:" , redis.hget("user.1", "name"))    
    print("email.1:" , redis.hget("user.1", "email"))  
    print("-------------")

    #hset(key, field, value) hget()
    redis.hset("user.2", "name1", "peter")    
    print("map.2: ", redis.hgetall("user.2"))    
    print("type map.2: ", redis.type("user.2"))
    print("name.2:" , redis.hget("user.2", "name1"))        
    print("-------------")

    #delete all keys     
    for key in redis.scan_iter("prefix:*"):
        redis.delete(key)


def list_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("LIST")
    print("-------------")

    #lpush(name, *values) - in initial position
    redis.lpush("names","pedro" " ana" " mara")
    print("names: ", redis.lrange("names", 0, 2))   

    #delete all keys     
    for key in redis.scan_iter("prefix:*"):
        redis.delete(key)


def sets_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("SETS")
    print("-------------")

    #sadd(name, *values)  
    redis.sadd("telephone", 938293287, 329832932)
    print(redis.smembers("telephone"))

    #delete all keys     
    for key in redis.scan_iter("prefix:*"):
        redis.delete(key)

def sorted_sets_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("SORTED_SETS")
    print("-------------")

    #zadd(name,mapping) zrangebyscore(name, min, max)
    redis.zadd("country.user", {392832938: 0, 34340923233: 1})
    print(redis.zrangebyscore("country.user", 0, 1))

    #delete all keys     
    for key in redis.scan_iter("prefix:*"):
        redis.delete(key)

    #clean data
    redis.flushdb

def main():        
    import sys 
    #start redis-server
    import os
    try:     
        #run redis before python   
        os.system('redis-server')        
        strings_redis()
        hashes_redis()
        list_redis()
        sets_redis()
        sorted_sets_redis()
    except Exception:      
        e = sys.exc_info()[1]  
        print(e.args[0])
    
if __name__ == '__main__':    
    main()       