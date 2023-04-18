
from django.urls import path

from .views import (
    OffersList , OffersDetail
)

urlpatterns = [
    path('' , OffersList.as_view(), name='offers'),
    path('<int:pk>' , OffersDetail.as_view(), name='offers'),
]
