from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm


def home_view(request):
    context = {'form': SaleSearchForm()}
    return render(request=request, template_name="sales/home.html", context=context)


class SalesListView(ListView):
    model = Sale
    template_name = "sales/sales_list.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/sale_detail.html'
