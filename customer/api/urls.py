
from django.urls import path

from .views import (
    OffersList , 
    OffersDetail, 
    MarketerList, 
    MarketerDetail
)

urlpatterns = [
    path('crud/' , OffersList.as_view(), name='offer_customer'),
    path('crud/<int:pk>' , OffersDetail.as_view(), name='offer_customer'),
    path('offers/' , MarketerList.as_view() , name='offer_marketer'),
    path('offers/<int:pk>' , MarketerDetail.as_view() , name='offer_marketer')
]
