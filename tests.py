import pytest

@pytest.fixture()
def dict_setup(request):
    dict1 = {"John": 1.9, "Mark": 1.85, "Jack": 1.81}
    return dict1

def test_negative_dict(dict_setup):
	try:
		assert dict_setup["Sally"]
	except KeyError:
		pass

def test_dict_values(dict_setup):
	assert (abs(dict_setup["John"] - 1.9) < 0.1)
	assert (abs(dict_setup["Mark"] - 1.85) < 0.1)
	assert (abs(dict_setup["Jack"]*5 - 9.05) < 0.1)

@pytest.mark.parametrize("key, is_present", [("John", True), ("Mark", True), ("Sally", False), ("Danny", False)])
def test_dict_keys(dict_setup, key, is_present):
	assert((key in dict_setup) == is_present)

