from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views import generic
from .models import Auction
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AuctionForm


class AuctionListView(LoginRequiredMixin, generic.ListView):
    model = Auction
    paginate_by = 10
    template_name='auction.html'
    login_url = 'accounts/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class AuctionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Auction
    template_name = 'auction_form.html'
    form_class = AuctionForm
    success_url = reverse_lazy('auction:auction-list')

    def form_valid(self, form: AuctionForm) -> HttpResponse:
        user = get_user_model().objects.get(id=self.request.user.id)
        form.instance.user = user
        form.instance.time_ending = datetime.now()+timedelta(days=5)
        form.instance.number_of_bids = 3
        return super(AuctionCreateView, self).form_valid(form)