import pytest

from racetest.race import Race

N_MODELS_PER_RACE = 2

@pytest.fixture()
def race(request, random_seed):
    return Race(random_seed)


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def mustang(request, race):
  return race.mustangs[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def fiesta(request, race):
  return race.fiestas[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def wrx(request, race):
  return race.wrxs[request.param]


@pytest.fixture(params=list(range(N_MODELS_PER_RACE)))
def liberty(request, n):
  return race.liberties[request.param]
