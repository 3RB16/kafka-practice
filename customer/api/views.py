from django.shortcuts import get_object_or_404
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Offer
from .serializers import OffersSerializer

import json
from django.core.serializers import serialize

from kafka import KafkaProducer

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

class OffersList(APIView):
    def get(self, request):
        offer_data = OffersSerializer(Offer.objects.all() , many = True)
        return Response(offer_data.data , status= status.HTTP_200_OK)
    
    def post(self, request):
        offer_data = OffersSerializer(data = request.data)
        if offer_data.is_valid():
            offer_data.save()
            return Response(offer_data.data , status = status.HTTP_201_CREATED)
        return Response(offer_data.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        Offer.objects.all().delete()
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)

class OffersDetail(APIView):
    def get(self, request, pk):
        try:
            offer_data = OffersSerializer(Offer.objects.get(id = pk))
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(offer_data.data , status=status.HTTP_302_FOUND)
    
    def put(self, request, pk):
        try:
            offer_data = OffersSerializer(data = request.data,instance = Offer.objects.get(id = pk))    
            if offer_data.is_valid():
                offer_data.save()
                return Response(data = {'message' : 'Offer updated'} , status=status.HTTP_200_OK)
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(offer_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            Offer.objects.get(id = pk).delete()
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(data = {'message' : 'Offer deleted'} , status = status.HTTP_200_OK)
    
class MarketerList(APIView):
    def get(self, request):
        offer_data = OffersSerializer(Offer.objects.all() , many = True)
        return Response(offer_data.data , status= status.HTTP_200_OK)
    
    def post(self, request):
        offer_data = OffersSerializer(data = request.data)
        if offer_data.is_valid():
            producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                api_version=(0,11,5),
                value_serializer=lambda x: json.dumps(x).encode('utf-8'))
            offer_json = json.loads(json.dumps(request.data))
            offer_json['type'] = 'create-offer'
            try:
                producer.send("offers", offer_json)
            except Exception as e:
                logger.error(e)
            finally:
                producer.flush()
            return Response(offer_data.data , status = status.HTTP_201_CREATED)
        return Response(offer_data.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        Offer.objects.all().delete()
        return Response(data = {'message' : 'deleted'} , status = status.HTTP_200_OK)
    
class MarketerDetail(APIView):
    def get(self, request, pk):
        try:
            offer_data = OffersSerializer(Offer.objects.get(id = pk))
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        return Response(offer_data.data , status=status.HTTP_302_FOUND)
    
    def put(self, request, pk):
        try:
            offer_data = OffersSerializer(data = request.data,instance = Offer.objects.get(id = pk))    
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        if offer_data.is_valid():
            producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
            api_version=(0,11,5),
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))
            offer_json = json.loads(json.dumps(request.data))
            offer_json['id'] = pk
            offer_json['type'] = 'update-offer'
            try:
                producer.send("offers", offer_json)add .
            except Exception as e:
                logger.error(e)
            finally:
                producer.flush()
            return Response(data = {'message' : 'Offer updated'} , status=status.HTTP_200_OK)
        return Response(offer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            offer_data = Offer.objects.get(id=pk)
        except Offer.DoesNotExist:
            return Response(data = {'message' : 'Offer not found'} , status=status.HTTP_404_NOT_FOUND)
        producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                api_version=(0,11,5),
                value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        offer_json = json.loads(json.dumps({
            'id': offer_data.id,
            'name': offer_data.name,
            'price': format(offer_data.price, ".2f"),
            'description':offer_data.description,
            'type':'delete-offer',
        }))
        try:
            producer.send("offers", offer_json)
        except Exception as e:
            logger.error(e)
        finally:
            producer.flush()
        return Response(data = {'message' : 'Offer deleted'} , status=status.HTTP_200_OK)

