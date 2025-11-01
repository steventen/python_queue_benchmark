import asyncio
import os
import time

from tasks import app, load_test_job


total_jobs = int(os.getenv("TOTAL_JOBS", 20000))


async def enqueue_jobs():
    async with app.open_async():
        start_time = time.time()
        for i in range(total_jobs):
            print(f"Enqueuing job {i}")
            await load_test_job.defer_async(num=i)
        end_time = time.time()
        print("All jobs enqueued within: ", end_time - start_time, "seconds")


if __name__ == "__main__":
    asyncio.run(enqueue_jobs())

