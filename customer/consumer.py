import json

from kafka import KafkaConsumer

from api.models import Offer
from api.serializers import OffersSerializer


# Create a Kafka consumer.
consumer = KafkaConsumer(
    'offers',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group',
)

# Subscribe to the topic.
consumer.subscribe(['offers'])

# Loop over the messages.
for message in consumer:

    # Display the offer on the console.
    print(message.value)

    # Get the key of the message.
    key = message.key
    offer = json.loads(message.value)
    # Determine the request type.
    if key == 'create-offer':
        # The request is to create an offer.
        offer_model = OffersSerializer(data = offer)
        if offer_model.is_valid():
            offer_model.save()
        else:
            print("bug here")
            
    elif key == 'update-offer':
        # The request is to update an offer.
        try:
            offer_model = OffersSerializer(data = offer,instance = Offer.objects.get(id = offer['id']))    
            if offer_model.is_valid():
                offer_model.save()
        except Offer.DoesNotExist:
            print("bug here")
    elif key == 'delete-offer':
        # The request is to delete an offer.
        try:
            Offer.objects.get(id = offer['id']).delete()
        except Offer.DoesNotExist:
            print("bug here")
# Close the consumer.
consumer.close()
