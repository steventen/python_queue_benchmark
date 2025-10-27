import time
from taskiq_redis import RedisStreamBroker

broker = RedisStreamBroker(url="redis://localhost:6379")


@broker.task
async def load_test_job(num):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
    return
