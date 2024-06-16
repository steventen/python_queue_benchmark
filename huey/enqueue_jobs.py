import os
import time
from tasks import load_test_job


total_jobs = os.getenv("TOTAL_JOBS", 20000)


def enqueue_jobs():
    start_time = time.time()
    for i in range(total_jobs):
        print(f"Enqueuing job {i}")
        load_test_job(i)
    end_time = time.time()
    print("All jobs enqueued within: ", end_time - start_time, "seconds")


if __name__ == "__main__":
    enqueue_jobs()
