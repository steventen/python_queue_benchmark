import time
from celery_config import app


@app.task
def load_test_job(num):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
    return
