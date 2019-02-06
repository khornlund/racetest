import pytest


N_SEEDS = 10

def pytest_generate_tests(metafunc):
    if 'random_seed' in metafunc.fixturenames:
        metafunc.parametrize('random_seed', list(range(N_SEEDS)))
