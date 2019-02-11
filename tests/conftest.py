import pytest


N_SEEDS = 10

def pytest_generate_tests(metafunc):
    if 'random_seed' in metafunc.fixturenames:
        metafunc.parametrize('random_seed', list(range(N_SEEDS)))

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.race = item.funcargs['race'].name
#     if 'mustang' in item.funcargs:
#         report.model = 'mustang'
#     if 'fiesta' in item.funcargs:
#         report.model = 'fiesta'
