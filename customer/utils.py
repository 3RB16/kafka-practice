from api.models import Offer
from api.serializers import OffersSerializer

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

# The request is to create an offer.
def create_offer(offer):
    offer_model = OffersSerializer(data = offer)
    if offer_model.is_valid():
        offer_model.save()
        logger.info('offer created successfully')
        return 
    logger.error('offer not created')

# The request is to update an offer.
def update_offer(offer):
    try:
        offer_model = OffersSerializer(data = offer,instance = Offer.objects.get(id = offer['id']))    
        if offer_model.is_valid():
            offer_model.save()
            logger.info('offer updated successfully')
    except Offer.DoesNotExist:
        logger.error('offer Does Not Exist')

# The request is to delete an offer.
def delete_offer(offer):
    try:
        Offer.objects.get(id = offer['id']).delete()
        logger.info('offer deleted successfully')
    except Offer.DoesNotExist:
        logger.error('offer Does Not Exist')