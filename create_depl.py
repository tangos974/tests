from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/tangos974/tests",
        entrypoint="test.py:test_flow",
    ).deploy(
        name="my-first-deployment",
    )
