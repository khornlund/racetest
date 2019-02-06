import pytest


N_SEEDS = 10

def pytest_generate_tests(metafunc):
    if 'random_seed' in metafunc.fixturenames:
        metafunc.parametrize('random_seed', list(range(N_SEEDS)))

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.race = item.funcargs['race'].name
    # attrs = [attr for attr in dir(item)]
    # print('Item attributes:')
    # for attr in attrs:
    #     try:
    #         attr_val = str(item.attr)
    #         if 'mustang' in attr_val:
    #             print(f'{attr}: {attr_val}')
    #     except:
    #         pass

    # report.language = f'{lang.title()}'
    # report.lib = lib
