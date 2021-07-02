from django.shortcuts import render
from django.views.generic import ListView

from .models import Order, Product


class OrderListView(ListView):
    model = Order
