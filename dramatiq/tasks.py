import time
import dramatiq


@dramatiq.actor
def load_test_job(num):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
    return
