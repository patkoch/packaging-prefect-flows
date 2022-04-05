import prefect
from prefect import task, Flow
from prefect.storage import Azure
from prefect.storage import GitHub

STORAGE = GitHub(
    repo="patkoch/packaging-prefect-flows",
    path=f"flows/my-example-flow.py",
)
    
@task
def example_task():
    logger = prefect.context.get("logger")
    logger.info("Hello!")
    
with Flow("my-example-flow", storage=STORAGE) as flow:
    example_task()