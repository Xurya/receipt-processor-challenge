import pytest
from utils.utils import alpha_numeric_count, is_multiple

# Alpha Numeric Count Unit Tests

def test_valid_alpha_numeric_count():
    assert alpha_numeric_count("abcDEFzZnEpA1234567890") == 22

def test_invalid_alpha_numeric_count():
    with pytest.raises(TypeError):
        alpha_numeric_count(12345)

def test_empty_alpha_numeric_count():
    assert alpha_numeric_count("") == 0

def test_zero_alpha_numeric_count():
    assert alpha_numeric_count("!@#$%^&*()-=_+`~\|;") == 0

def test_spaced_alpha_numeric_count():
    assert alpha_numeric_count("abc def 12345") == 11

def test_varied_alpha_numeric_count():
    assert alpha_numeric_count("a';@3#b95x  -=!^&*") == 6

# Is Multiple Unit Tests

def test_valid_is_multiple():
    assert is_multiple(5, 1)

def test_invalid_is_multiple():
    with pytest.raises(TypeError):   
        is_multiple("abc", "def")

def test_zero_is_multiple():
    with pytest.raises(ZeroDivisionError): 
        is_multiple(5, 0)

def test_not_is_multiple():
    assert not is_multiple(5,3)

def test_large_is_multiple():
    assert is_multiple(1527696, 1236)

def test_not_large_is_multiple():
    assert not is_multiple(52234549203, 3578)