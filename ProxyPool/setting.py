# 设置代理的分数值
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

#设置代理池的数量
POOL_UPPER_THRESHOLD = 10000


# redis数据库
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_KEY = 'proxies'



# 测试API
TEST_URL = 'https://www.baidu.com'
# API配置
API_HOST = 'localhost'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300




VALID_STATUS_CODES = [200, 302]
