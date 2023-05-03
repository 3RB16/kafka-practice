
from django.urls import path

from .views import (
    OffersList , OffersDetail, Marketer
)

urlpatterns = [
    path('crud/' , OffersList.as_view(), name='offer_customer'),
    path('crud/<int:pk>' , OffersDetail.as_view(), name='offer_customer'),
    path('offers/' , Marketer.as_view() , name='offer_marketer'),
    path('offers/<int:pk>' , Marketer.as_view() , name='offer_marketer')
]
