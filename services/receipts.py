import math
from typing import List
from models.models import Receipt, Item
from utils.utils import alpha_numeric_count, is_multiple
import uuid

# Memory storage, no database as per requirements
receipt_db = {}

def get_receipt(id: str) -> Receipt:
    '''Getter function for receipts from 'database' given a UUID'''
    return receipt_db[id]

def update_points(id: str, points: int) -> None:
    '''Update rewarded points for a receipt'''
    receipt_db[id].points = points

def create_receipt(retailer: str, purchase_date: str, purchase_time: str, items: List[dict], total: str) -> Receipt:
    '''Create receipt from data for preparation and storage'''
    # request schema requires minItems: 1 
    if not items: 
        raise Exception("Receipt has no items")

    # item model
    item_list: List[Item] = []
    for item in items:
        item_list.append(Item(item['shortDescription'], item['price']))
    
    # receipt model
    return Receipt(retailer, purchase_date, purchase_time, item_list, total)

def save_receipt(receipt: Receipt) -> str:
    '''Save receipt in memory, mapped to a UUID'''
    # generate unique receipt id, as if we have database
    receipt_id = str(uuid.uuid4())

    # 'save' to database
    receipt_db[receipt_id] = receipt

    return receipt_id

def item_description_points(items: List[Item]) -> int:
    '''Given a list of Items, return number of points rewarded'''
    points = 0
    for item in items:
        if is_multiple(len(item.short_description.strip()), 3):
            points += math.ceil(float(item.price) * 0.2)
    return points

def purchase_date_points(purchase_date: str) -> int:
    '''Given a purchase date, reward 6 points if the day in the purchase date is odd'''
    return 6 if int(purchase_date.split("-")[2]) % 2 == 1 else 0

def purchase_time_points(purchase_time: str) -> int:
    '''Given a purchase time, reward 10 points if the time of purchase is after 2:00pm and before 4:00pm.'''
    return 10 if 14 <= int(purchase_time.split(":")[0]) < 16 else 0

def calculate_points(receipt: Receipt) -> int:
    '''Given a prepared receipt, calculate the total number of points to be rewarded based on criteria.
    
    For more information on scoring and rules, refer to the Challenge Prompt.
    '''
    points = 0;

    # One point for every alphanumeric character in the retailer name
    points += alpha_numeric_count(receipt.retailer)
    
    # 50 points if the total is a round number amount with no cents
    total = float(receipt.total)
    if (is_multiple(total, 1)):
        points += 50
    
    # 25 points if the total is a multiple of 0.25
    if (is_multiple(total, 0.25)):
        points += 25
    
    # 5 points for every two items on the receipt
    points += len(receipt.items)//2 * 5

    # If the trimmed length of the item description is a multiple of 3, multiply the price by `0.2` and round up to the nearest integer. The result is the number of points earned.
    points += item_description_points(receipt.items)

    # 6 points if the day in the purchase date is odd.
    points += purchase_date_points(receipt.purchase_date)

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    points += purchase_time_points(receipt.purchase_time)

    return points

