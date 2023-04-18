from django.test import TestCase,RequestFactory

from .models import Offer
from .views import (
    OffersList, OffersDetail
)
from .serializers import OffersSerializer

class OffersTest(TestCase):
    def setUp(self):
        Offer.objects.create(name="manga",price=4,description="Manga discount offer, 30% off")
        Offer.objects.create(name="frawla",price=4,description="frawla discount offer, 20% off")
    
    def test_post(self):  
        offer1 = OffersSerializer(Offer.objects.get(id=1))
        self.assertEqual(offer1.data,{"id":1,"name":"manga","price":format(4, ".2f"),"description":"Manga discount offer, 30% off"}) 
    
    def test_get_all(self):
        request = RequestFactory().get('/offers/')
        response = OffersList.as_view()(request)
        all_offers = OffersSerializer(Offer.objects.all(),many=True)
        self.assertEqual(all_offers.data,response.data)

    def test_delete_all(self):
        Offer.objects.all().delete()
        self.assertTrue(len(Offer.objects.filter(id=1)) == 0)
        self.assertTrue(len(Offer.objects.filter(id=2)) == 0)


