from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import generic

from .forms import AuctionForm
from .models import Auction, Bid


class AuctionListView(LoginRequiredMixin, generic.ListView):
    model = Auction
    paginate_by = 10
    template_name='auction/auction.html'
    # login_url = 'accounts/login'

    def get_context_data(self, **kwargs):
        print(dir(self))
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class AuctionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Auction
    template_name = 'auction/auction_form.html'
    form_class = AuctionForm
    success_url = reverse_lazy('auction:auction-list')

    def form_valid(self, form: AuctionForm) -> HttpResponse:
        user = get_user_model().objects.get(id=self.request.user.id)
        form.instance.user = user
        form.instance.time_ending = datetime.now()+timedelta(days=5)
        return super(AuctionCreateView, self).form_valid(form)


class AuctionDetailsView(generic.DetailView):
    model = Auction


def bid_raise(request, auction_id):
    user = get_user_model().objects.get(id=request.user.id)

    auction = Auction.objects.get(id=auction_id)
    min_bid = auction.min_bid
    # raise by 1/10th for every time a bid is place
    raised_bid = min_bid + (min_bid / 10)
    auction.min_bid = raised_bid
    auction.save()
    Bid.objects.create(auction=auction, user=user)
    messages.success(request, "Bid has been added succesfully")
    return redirect(reverse('auction:auction-list'))
