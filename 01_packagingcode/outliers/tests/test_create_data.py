import numpy as np
import pytest
import outliers.utils.data

'''
code for testing the package, using pytest.
always start or end the file with test like "test_..." or "..._test".
this test will end up as SUCCESS test because of the nature of the program.
'''

# a fixture decorator -> preconditions for a test, provide data, or perform a teardown after a test is finished

@pytest.fixture()
def dummy_data():
    data = outliers.utils.data.create_data()
    return data


def test_data_is_numpy(dummy_data):
    assert isinstance(dummy_data, np.ndarray)


def test_data_is_large(dummy_data):
    assert len(dummy_data) > 100