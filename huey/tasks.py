import time
from huey import RedisHuey

huey = RedisHuey()


@huey.task()
def load_test_job(num):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
