import time
from arq.connections import RedisSettings


async def load_test_job(ctx, num):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
    return


class WorkerSettings:
    functions = [load_test_job]
    redis_settings = RedisSettings()
    poll_delay = 0.01
    max_jobs = 1000
