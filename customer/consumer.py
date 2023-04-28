import json

from kafka import KafkaConsumer

from utils import (
    create_offer, update_offer, delete_offer
)

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
        create_offer(offer)    
    elif key == 'update-offer':
        update_offer(offer)
    elif key == 'delete-offer':
        delete_offer(offer)
# Close the consumer.
consumer.close()
