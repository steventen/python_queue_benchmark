import asyncio
import os
import time
from tasks import broker, load_test_job

total_jobs = int(os.getenv("TOTAL_JOBS", 20000))


async def enqueue_jobs():
    await broker.startup()
    start_time = time.time()
    for i in range(total_jobs):
        print(f"Enqueuing job {i}")
        await load_test_job.kiq(i)
    end_time = time.time()
    print("All jobs enqueued within: ", end_time - start_time, "seconds")
    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(enqueue_jobs())
