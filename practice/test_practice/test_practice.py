from datetime import datetime

import pytest
import requests


class TestFirstClass:
    def test_first(self):
        print('This is test')

    def test_failing_test(self):
        response = requests.get("https://github.com/")
        status_code_actual = response.status_code
        status_code_expected = 404

        assert status_code_actual == status_code_expected

    def test_failing_test(self):
        response = requests.get("https://github.com/")
        status_code_actual = response.status_code
        status_code_expected = 404

        assert status_code_actual == status_code_expected

    @pytest.mark.skip
    def test_failing_test_skipped(self):
        response = requests.get("https://github.com/")
        status_code_actual = response.status_code
        status_code_expected = 404

        assert status_code_actual == status_code_expected

    @pytest.mark.skipif(
        int(datetime.now().timestamp()) % 2 == 0,
        reason="Time stamp is even"
    )
    def test_failing_test_skipped_condition(self):
        response = requests.get("https://github.com/")
        status_code_actual = response.status_code
        status_code_expected = 404

        assert status_code_actual == status_code_expected

    @pytest.mark.xfail
    def test_failing_test_xfail(self):
        response = requests.get("https://github.com/")
        status_code_actual = response.status_code
        status_code_expected = 404

        assert status_code_actual == status_code_expected
