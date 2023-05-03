import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer.settings')

import django
django.setup()

import json
from json import loads

from kafka import KafkaConsumer

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

def consumer():
    # Create a Kafka consumer.
    consumer = KafkaConsumer(
        'offers',
        bootstrap_servers='kafka:9092',
        api_version=(0,11,5),
        auto_offset_reset='earliest',
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    # Subscribe to the topic.
    consumer.subscribe(['offers'])

    # Loop over the messages.
    for message in consumer:
        # Display the offer on the console.
        print(message.value)
        offer = message.value
        key = offer['type']
        offer.pop('type' , None)
        # Determine the request type.
        if key == 'create-offer':
            create_offer(offer)    
        elif key == 'update-offer':
            update_offer(offer)
        elif key == 'delete-offer':
            delete_offer(offer)
    # Close the consumer.
    consumer.close()

if __name__ == "__main__":
    consumer()