import random

import pytest





@pytest.mark.parametrize("first_name", ["John", "Harry", "Ron", "Hermione"])
@pytest.mark.parametrize("last_name", ["Smith", "Potter", "Weasley", "Granger"])
class TestHomework:

    @pytest.mark.wizard
    def test_fail_if_john_smith(self, age, first_name, last_name):
        print(f"Hello {first_name} {last_name}! Your age is {age}")
        if first_name == "John" and last_name == "Smith":
            pytest.xfail("This test is expected to fail for John Smith")
