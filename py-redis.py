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

    #set()
    redis.set("name","javier")    
    redis.set("name","jaime")  
    print("key: ", redis.get("nombre"))  
    print("-------------")
    print("keys: ", redis.keys())  
    print("-------------")

    #setnx()
    redis.set("name","javier")    

    #mset()
    redis.mset({"name": "peter", "name": "david"})    
    print("name: ", redis.mget("name"))         
    print("-------------")

   
def hashes_redis():
    import redis    
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("HASH")
    print("-------------")

    #hmset() hget() hgetall()
    redis.hmset("user.1", {"name": "peter", "email": "siuuds@gmail.com"})    
    print("map.1: ", redis.hgetall("user.1"))    
    print("name.1:" , redis.hget("user.1", "name"))    
    print("email.1:" , redis.hget("user.1", "email"))  
    print("-------------")

    #hset(key, field, value) hget()
    redis.hset("user.2", "name1", "peter")    
    print("map.2: ", redis.hgetall("user.2"))    
    print("name.2:" , redis.hget("user.2", "name1"))    
    #print("email.2:" , redis.hget("user.2", "email"))  
    print("-------------")


def list_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("LIST")
    print("-------------")

    #lpush() - initial    
    redis.lpush("names","pedro" " ana" " mara")
    print("names: ", redis.lrange("names", 0, 2))   



def sets_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("SETS")
    print("-------------")



def sorted_sets_redis():
    import redis
    redis = redis.Redis(host='127.0.0.1', port=6379, db=0, charset="utf-8", decode_responses=True)
    print("-------------")
    print("SORTED_SETS")
    print("-------------")





def main():        
    import sys 
    strings_redis()
    hashes_redis()
    list_redis()
    sets_redis()
    sorted_sets_redis()

if __name__ == '__main__':    
    main()       