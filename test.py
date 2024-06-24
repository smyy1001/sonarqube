import os.path
import sys
import pytest

sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), '..'))


def pytest_runtest_setup(item):
    # called for running each test in 'current' directory
    print("setting up", item)


@pytest.fixture(scope='session')
def global_fixture():
    """
    Fixtures are callables decorated with @fixture
    """
    print("\n(global_fixture)")


@pytest.fixture(scope='session')
def env_vars():
    return {
    }

@pytest.fixture(scope='session')
def mock_data():
    return 
    }