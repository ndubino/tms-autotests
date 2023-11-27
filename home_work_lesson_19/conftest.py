import random
import pytest


@pytest.fixture()
def age():
    number = random.randint(0, 100)
    print(f'Random age is {number}')
    yield number
    print('Deleting random age... Done')