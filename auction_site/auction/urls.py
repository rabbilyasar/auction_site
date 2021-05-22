from django.urls import path
from .views import AuctionListView, AuctionCreateView

app_name = 'auction'

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction-list'),
    path('add/', AuctionCreateView.as_view(), name='auction-create')
]
