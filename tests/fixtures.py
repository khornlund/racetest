import pytest

from racetest.race import Race

N_MODELS_PER_RACE = 2

@pytest.fixture()
def race(request, random_seed, json_metadata):
    json_metadata['random_seed'] = random_seed
    return Race(random_seed)


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def mustang(request, race, json_metadata):
    json_metadata['model'] = 'mustang'
    return race.mustangs[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def fiesta(request, race, json_metadata):
    json_metadata['model'] = 'fiesta'
    return race.fiestas[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def wrx(request, race, json_metadata):
    json_metadata['model'] = 'wrx'
    return race.wrxs[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def liberty(request, race, json_metadata):
    json_metadata['model'] = 'liberty'
    return race.liberties[request.param]
