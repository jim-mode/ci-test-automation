import allure
import pytest

@allure.feature('Feature1')
@allure.story('Story1')
def test_capitalize_string_01():
    assert capitalize_string('test') == 'Test'

@allure.feature('Feature2')
@allure.story('Story2', 'Story3')
@allure.story('Story4')
class TestCap:
    def test_capitalize_string_02(self):
        assert capitalize_string('python') == 'Python'

@allure.feature('Feature3')
@pytest.mark.fruits
def test_capitalize_string_03():
    assert capitalize_string('apple') != 'Pear'

@allure.feature('Random Fail')
def test_random_fail():
    assert randint(0,1) == 1

def capitalize_string(s):
  if not isinstance(s, str):
    raise TypeError('Please provide a string')
  return s.capitalize()
