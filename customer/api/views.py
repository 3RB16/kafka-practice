from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Offer
from .serializers import OffersSerializer

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