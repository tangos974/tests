from prefect import flow, task


@task(log_prints=True)
def regenerate_urls() -> str:
    return "toto"


@flow(log_prints=True)
def test_flow():
    s = regenerate_urls()
    print(s)


if __name__ == "__main__":
    test_flow()
