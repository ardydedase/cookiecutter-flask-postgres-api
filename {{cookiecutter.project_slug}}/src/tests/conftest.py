import pytest


from app import create_app


@pytest.yield_fixture(scope='function')
def app():
    return create_app()
