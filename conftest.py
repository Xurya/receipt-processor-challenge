import pytest
from services.receipts import create_receipt, save_receipt
from controllers.receipts import process_receipt

@pytest.fixture(scope='session')
def simple_process():
    return process_receipt("abc", "2022-01-21", "15:02", [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        }
    ], "6.49")

@pytest.fixture(scope='session')
def simple_receipt():
    receipt = create_receipt('Target', '2022-01-02', '13:13', [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
    ], '1.25')
    return receipt

@pytest.fixture(scope='session')
def simple_save(simple_receipt):
    return save_receipt(simple_receipt)

@pytest.fixture(scope='session')
def morning_receipt():
    receipt = create_receipt('Walgreens', '2022-01-02', '08:13', [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ], '2.65')
    return receipt

@pytest.fixture(scope='session')
def example_receipt():
    receipt = create_receipt('Target', '2022-01-01', '13:01', [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ], '35.35')
    return receipt

@pytest.fixture(scope='session')
def example_receipt_two():
    receipt = receipts.create_receipt('M&M Corner Market', '2022-03-20', '14:33', [
        {
            "shortDescription": "Gatorade",
            "price": "2.25"
        },{
            "shortDescription": "Gatorade",
            "price": "2.25"
        },{
            "shortDescription": "Gatorade",
            "price": "2.25"
        },{
            "shortDescription": "Gatorade",
            "price": "2.25"
        }
    ], '9.00')
    return receipt