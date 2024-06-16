# Load Benchmark on Various Task Queues in Python

The task queue libraries in this benchmark:

- **RQ (Redis Queue)**
- **ARQ (Async Redis Queue)**
- **Celery**
- **Huey**
- **Dramatiq**

## Test Method

The benchmark is very naive, it measure the total time spent on processing `20,000` jobs by `10` workers. Each job simply prints the current time.

All tests were conducted on a MacBook Pro 14 inch M2 Pro with 16GB of RAM.

## Prerequisites

Before running the tests, ensure you have Docker installed. Start Redis using Docker Compose:

```bash
docker compose up
```

Install [pdm](https://pdm-project.org/en/latest/#installation), and then run:

```bash
pdm install
```

## RQ

[RQ Documentation](https://python-rq.org/)

1. Navigate to the RQ directory:
   ```bash
   cd rq
   ```
2. Enqueue the jobs:
   ```bash
   python enqueue_jobs.py
   ```
3. Process jobs:
   ```bash
  python -c "import time; print(f'Start time: {time.time()}')" > time.log && rq worker-pool -q -n 10
  ```
4. Record the time when the last job finishes and note the start time in `time.log`.
5. Calculate the difference.

### Results

- All jobs enqueued within: 4.03 seconds
- With 10 workers, finished in 51.05 seconds


## ARQ

[ARQ Documentation](https://arq-docs.helpmanual.io/)

1. Navigate to the ARQ directory:
   ```bash
   cd arq
   ```
2. Enqueue the jobs:
   ```bash
   python enqueue_jobs.py
   ```
3. ARQ has no built-in support for running multiple workers, so we use `supervisord`:
  ```bash
    python -c "import time; print(f'Start time: {time.time()}')" > time.log && supervisord -c supervisord.conf
  ```
4. Record the time when the last job finishes and note the start time in `time.log`.
5. Calculate the difference.

### Results

- All jobs enqueued within: 9.34 seconds
- With 10 workers, finished in 35.37 seconds


## Celery

[Celery Documentation](https://docs.celeryq.dev/en/main/getting-started/introduction.html)

1. Navigate to the Celery directory:
   ```bash
   cd celery
   ```
2. Enqueue the jobs:
   ```bash
   python enqueue_jobs.py
   ```
3. Process jobs:
```bash
python -c "import time; print(f'Start time: {time.time()}')" > time.log && celery -q --skip-checks -A tasks worker --loglevel=info -c 10 -P threads
```
4. Record the time when the last job finishes and note the start time in `time.log`.
5. Calculate the difference.

### Results

- All jobs enqueued within: 6.34 seconds
- With 10 thread workers, finished in 11.68 seconds
- With 10 process workers (`-P processes`), finished in 17.60 seconds



## Huey

[Huey Documentation](https://huey.readthedocs.io/en/latest/)

1. Navigate to the Huey directory:
   ```bash
   cd huey
   ```
2. Enqueue the jobs:
   ```bash
   python enqueue_jobs.py
   ```
3. Process jobs:
   ```bash
   python -c "import time; print(f'Start time: {time.time()}')" > time.log && huey_consumer.py tasks.huey -k thread -w 10 -d 0.001 -C -q
   ```
4. Record the time when the last job finishes and note the start time in `time.log`.
5. Calculate the difference.

### Results

- All jobs enqueued within: 2.40 seconds
- With 10 thread workers, finished in 4.15 seconds
- With 10 process workers (`-k process -w 10 -d 0.001 -C -q`), finished in 3.18 seconds

## Dramatiq

[Dramatiq Documentation](https://dramatiq.io/index.html)

1. Navigate to the Dramatiq directory:
   ```bash
   cd dramatiq
   ```
2. Enqueue the jobs:
   ```bash
   python enqueue_jobs.py
   ```
3. Process jobs:
   ```bash
   python -c "import time; print(f'Start time: {time.time()}')" > time.log && dramatiq tasks -p 1 -t 10
   ```
4. Record the time when the last job finishes and note the start time in `time.log`.
5. Calculate the difference.

### Results

- All jobs enqueued within: 3.27 seconds
- With 1 process and 10 threads, finished in 4.12 seconds
- With default settings (10 processes, 8 threads), finished in 1.53 seconds