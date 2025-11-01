import time
from procrastinate import App, PsycopgConnector


# Use explicit DSN so it works out-of-the-box with docker-compose Postgres
app = App(
    connector=PsycopgConnector(
        conninfo="postgresql://postgres:password@localhost:5432/procrastinate"
    )
)


@app.task
async def load_test_job(num: int):
    end_time = time.time()
    print(f"Job {num} finished at {end_time}")
    return

