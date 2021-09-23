import pytest
import math

@pytest.fixture()
def dict_setup(request):
    dict1 = {"John": "skate", "Mark": "snowboard", "Jack": "bike"}
    return dict1

def test_negative_dict(dict_setup):
	try:
		assert dict_setup["Sally"]
	except KeyError:
		pass

def test_dict_values(dict_setup):
	assert (dict_setup["John"] == "skate")
	assert (dict_setup["Mark"] == "snowboard")
	assert (dict_setup["Jack"] == "bike")

@pytest.mark.parametrize("key, is_present", [("John", True), ("Mark", True), ("Sally", False), ("Danny", False)])
def test_dict_keys(dict_setup, key, is_present):
	assert((key in dict_setup) == is_present)

@pytest.mark.parametrize("num", [1.7, 1.5, 1.1, -1.1, -1.5, -1.7, 1.0, 0.0])
def test_float_rounding(num):
	assert (abs(round(num)-num) <= 0.5)
	frac, whole = math.modf(num)
	assert (abs(math.floor(num) + math.ceil(num) - num * 2 ) <= 1)
	assert (math.floor(num) <= math.ceil(num))
	assert (whole == int(num))

def test_float_limits():
	assert (10e9999 == math.inf)
	assert (-10e9999 == -math.inf)

@pytest.mark.parametrize("num, power, result", [(-10, -1.1, -0.07554+0.024546j),\
	(2, 3, 8), (16, 0.5, 4), (21.1, 0.3, 2.49623), (11.134, 5, 171102.3935)])
def test_pow_float_and_complex(num, power, result):
	assert(abs(pow(num, power).real-result.real) < 0.001)
	assert(abs(pow(num, power).imag-result.imag) < 0.001)
