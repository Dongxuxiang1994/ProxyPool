#崔的proxy池的redis的有序集合的操作存在问题
from redis import StrictRedis
from random import choice
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from setting import REDIS_KEY
import re
from error import PoolEmptyError


class RedisClient(object):
        def __init__(self, host='localhost', port=6379):
            self.db = StrictRedis(host=host, port=port, decode_responses=True)
            self.proxy_key = REDIS_KEY
        def add(self, proxy, score=INITIAL_SCORE):
            """增加代理"""
            if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
                print('代理不合规', proxy, '丢弃')
                return
            if not self.db.zscore(REDIS_KEY, proxy):
                #参考代码存在错误
                return self.db.zadd(REDIS_KEY, {proxy: score})

        def random(self):
            """随机取出一个最高分数的代理"""
            result=self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

        def decrease(self, proxy):
            """代理的score -1，当为最低分数时，移除"""
            score = self.db.zscore(REDIS_KEY, proxy)
            #还有个score指的是__init__的score，指代理的initial_score
            if score and score > MIN_SCORE:
                print('代理', proxy, '当前分数', score, '减1')
                return self.db.zincrby(REDIS_KEY, -1, proxy)
            else:
                print('代理', proxy, '当前分数', score, '移除')
                return self.db.zrem(REDIS_KEY, proxy)

        def exists(self, proxy):
            """判断是否存在"""
            return not self.db.zscore(REDIS_KEY, proxy) == None

        def max(self,proxy):
            """当代理有用时，设置为100分"""
            print('代理', proxy, '可用，设置为', MAX_SCORE)
            return self.db.zadd(REDIS_KEY, {proxy: MAX_SCORE})

        def count(self):
            """获取数量"""
            return self.db.zcard(REDIS_KEY)

        def all(self):
            """获取全部代理"""
            return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

        def batch(self, start, stop):
            """根据score从大到小排序，获取当中的一段"""
            return self.db.zrevrange(REDIS_KEY, start, stop - 1)


if __name__ == '__main__':
    conn = RedisClient()
    result = conn.batch(100, 150)
    print(result)
















