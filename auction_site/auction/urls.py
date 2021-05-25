from django.urls import path
from .views import AuctionListView, AuctionCreateView, AuctionDetailsView, bid_raise

app_name = 'auction'

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction-list'),
    path('add/', AuctionCreateView.as_view(), name='auction-create'),
    path('<int:pk>', AuctionDetailsView.as_view(), name='auction-details'),
    path('bid-raise/<int:auction_id>', bid_raise, name='raise-bid'),
]
