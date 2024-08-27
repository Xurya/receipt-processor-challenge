from typing import Dict, List
from services import receipts

def process_receipt(retailer: str, purchase_date: str, purchase_time: str, items: List[dict], total: str) -> Dict:
    '''Controller to process a receipt

    This controller takes the receipt information from the router, and saves a receipt in the database for processing. Then, points are calculated and rewarded from the receipt, and a unique ID is assigned and returned to the router.

    Parameters:
        - retailer (str) : The name of the retailer or store the receipt is from.
        - purchaseDate (str) : The date of the purchase printed on the receipt.
        - purchaseTime (str) : The time of the purchase printed on the receipt. 24-hour time expected.
        - items (List[Item]) : The list of items on the receipt. (For more details, see Item schema in api.yml)
        - total (str) : The total amount paid on the receipt.

    Returns:
        {
            id (str): id of the receipt
        }
    '''
    # Create receipt from data
    receipt = receipts.create_receipt(retailer, purchase_date, purchase_time, items, total)

    # save receipt to 'database' and obtain unique id
    receipt_id = receipts.save_receipt(receipt)

    # Calculate points awarded for the receipt
    points = receipts.calculate_points(receipt)

    # update 'database' with updated points
    receipts.update_points(receipt_id, points)

    return {'id': receipt_id}

def points(id: str) -> Dict:
    '''Controller to obtain points given an ID

    This route obtains the points rewarded from a processed receipt by its UUID.

    Parameters:
        - id (str) : id of the receipt

    Returns:
        {
            points (int) : Points rewarded from the receipt
        }
    '''

    # Get receipt from 'database' by it's uuid
    receipt = receipts.get_receipt(id)

    return {'points': receipt.points}