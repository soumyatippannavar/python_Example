import pytest


@pytest.fixture(scope="class")
def setup():
    print("use fixture")
    yield
    print("use yield")