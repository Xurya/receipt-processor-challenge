import pytest
from controllers import receipts

# Process Receipts

def test_valid_process_receipt(simple_process):
    assert 'id' in simple_process

def test_invalid_process_receipt():
    with pytest.raises(TypeError):
        receipts.process_receipt(12345, "2022-01-21", "15:02", [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }
        ], "6.49")
    
    with pytest.raises(IndexError):
        receipts.process_receipt("abc", "2022", "15:02", [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }
        ], "6.49")

    with pytest.raises(AttributeError):
        receipts.process_receipt("abc", "2022-01-21", {}, [
            {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
            }
        ], "6.49")

# Points

def test_valid_points(simple_process):
    assert receipts.points(simple_process['id']) == {'points': 19}

def test_invalid_points():
    with pytest.raises(Exception):
        receipts.points("abcd")