from flask import Blueprint, make_response, request, jsonify
from controllers import receipts
import logging

logger = logging.getLogger(__name__)

receipts_bp = Blueprint('receipts', __name__, url_prefix='/receipts')

@receipts_bp.route('/process', methods=['POST'])
def process():
    '''Route to process a receipt

    This route takes in a JSON receipt and returns a JSON object with a UUID4. The ID returned is the ID that should be passed into `/receipts/{id}/points` to get the number of points the receipt was awarded.

    Parameters:
        - retailer (str) : The name of the retailer or store the receipt is from.
        - purchaseDate (str) : The date of the purchase printed on the receipt.
        - purchaseTime (str) : The time of the purchase printed on the receipt. 24-hour time expected.
        - items (List[Item]) : The list of items on the receipt. (For more details, see Item schema in api.yml)
        - total (str) : The total amount paid on the receipt.

    Returns:
        - 200: Returns the ID assigned to the receipt
            {
                id (str): UUID4 id of the receipt
            }
        - 400: The receipt is invalid
    '''
    try:
        data = request.get_json(force=True)
        retailer = data['retailer']
        purchase_date = data['purchaseDate']
        purchase_time = data['purchaseTime']
        items = data['items']
        total = data['total']
        return make_response(receipts.process_receipt(retailer, purchase_date, purchase_time, items, total), 200)
    except Exception as e:
        logger.error('Exception while processing receipt: ', e)
        return make_response("The receipt is invalid", 400)

@receipts_bp.route('/<id>/points', methods=['GET'])
def points(id):
    '''Route to get points for a given receipt id

    This route obtains the points rewarded from a processed receipt by its UUID.

    Parameters:
        - id (str) : id of the receipt

    Returns:
        - 200: Returns the points rewarded for the receipt
            {
                points (int) : The number of points awarded
            }
        - 404: No receipt found for that id
    '''
    try:
        return make_response(receipts.points(id), 200)
    except Exception as e:
        logger.error('Exception while calculating points: ', e)
        return make_response("No receipt found for that id", 404)