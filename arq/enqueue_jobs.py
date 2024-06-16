import asyncio
import os
import time
from arq import create_pool
from arq.connections import RedisSettings
from tasks import load_test_job

total_jobs = os.getenv("TOTAL_JOBS", 20000)


async def enqueue_jobs():
    redis = await create_pool(RedisSettings())
    start_time = time.time()
    for i in range(total_jobs):
        print(f"Enqueuing job {i}")
        await redis.enqueue_job("load_test_job", i)
    end_time = time.time()
    print("All jobs enqueued within: ", end_time - start_time, "seconds")


if __name__ == "__main__":
    asyncio.run(enqueue_jobs())
