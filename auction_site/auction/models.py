from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self) -> str:
        return "email=" + self.user.email


# class Product(models.Model):
#     # user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
#     description = models.CharField(max_length=500)
#     quantity = models.IntegerField()
#     date_posted = models.DateTimeField(auto_now_add=True, blank=True)
#     #!todo category

#     def __str__(self) -> str:
#         return "user:" + self.user + "title:" + self.title


class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    min_bid = models.DecimalField(max_digits=6, decimal_places=2)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    number_of_bids = models.IntegerField(default=0)
    time_starting = models.DateTimeField(auto_now_add=True, blank=True)
    time_ending = models.DateTimeField()

    def __str__(self) -> str:
        return "user_id: " + str(self.user) + "title: " + str(self.title)

    @property
    def not_expired(self):
        return timezone.now() < self.time_ending


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    bid_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "USER_ID:" + str(self.user.id) + " AUCTION_ID:" + \
			str(self.auction.id) + " " + str(self.bid_time)