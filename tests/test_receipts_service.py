import pytest
from services import receipts
import uuid

def test_create_receipt(simple_receipt):
    assert simple_receipt.retailer == 'Target'
    assert simple_receipt.purchase_date == '2022-01-02'
    assert simple_receipt.purchase_time == '13:13'
    assert simple_receipt.items and simple_receipt.items[0].short_description == 'Pepsi - 12-oz'
    assert simple_receipt.items and simple_receipt.items[0].price == '1.25'

def test_create_receipt_empty_items():
    with pytest.raises(Exception):
        receipts.create_receipt('M&M Corner Market', '2022-03-20', '14:33', [], '9.00')

def test_get_valid_receipt(simple_receipt, simple_save):
    assert receipts.get_receipt(simple_save) == simple_receipt

def test_invalid_receipt():
    with pytest.raises(KeyError):
        assert receipts.get_receipt("abcde")

def test_save_receipt(simple_save, simple_receipt):
    assert uuid.UUID(simple_save, version=4)
    assert receipts.get_receipt(simple_save) == simple_receipt

# Examples

def test_points_processed_example_1(example_receipt):
    assert receipts.calculate_points(example_receipt) == 28

def test_points_processed_example_2(example_receipt_two):
    assert receipts.calculate_points(example_receipt_two) == 109

def test_morning_receipt(morning_receipt):
    assert receipts.calculate_points(morning_receipt) == 15

# Item description points

def test_valid_item_description_points(morning_receipt):
    assert receipts.item_description_points(morning_receipt.items) == 1

def test_invalid_description_item_description_points():
    with pytest.raises(AttributeError):
        receipts.item_description_points([{}])

def test_invalid_points_item_description_points():
    with pytest.raises(AttributeError):
        receipts.item_description_points([{"shortDescription": "Mountain Dew 12PK"}])

def test_varied_item_description_points(example_receipt):
    assert receipts.item_description_points(example_receipt.items) == 6

# Purchase Date points

def test_valid_purchase_date_points():
    assert receipts.purchase_date_points("2022-01-29") == 6
    assert receipts.purchase_date_points("2022-01-20") == 0

def test_invalid_purchase_date_points():
    with pytest.raises(AttributeError):
        receipts.purchase_date_points({})
    with pytest.raises(IndexError):
        receipts.purchase_date_points("2011-05")
    
# Purchase Time points

def test_valid_purchase_time_points():
    assert receipts.purchase_time_points("15:15") == 10
    assert receipts.purchase_time_points("10:10") == 0

def test_invalid_purchase_time_points():
    with pytest.raises(AttributeError):
        receipts.purchase_time_points({})