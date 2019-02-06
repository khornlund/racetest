import pytest

from fixtures import *

def test_mustang_engine_cylinders(mustang):
    assert mustang.engine.n_cylinders == 8

@pytest.mark.parametrize('wheel_num', [0,1,2,3])
def test_mustang_wheel_diameter_gt_14(mustang, wheel_num):
    wheel = mustang.wheels[wheel_num]
    assert wheel.diameter >= 14

def test_fiesta_engine_cylinders(fiesta):
    assert fiesta.engine.n_cylinders == 4

@pytest.mark.parametrize('wheel_num', [0,1,2,3])
def test_fiesta_wheel_diameter_gt_12(fiesta, wheel_num):
    wheel = fiesta.wheels[wheel_num]
    assert wheel.diameter >= 16