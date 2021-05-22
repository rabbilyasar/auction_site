from django import forms
from .models import Auction

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        exclude = ['number_of_bids', 'user', 'time_ending']

    def get_total_bids(self):
        return 1