from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm
import pandas as pd


def home_view(request):
    context = {}
    sales_df = None
    positions_df = None

    if request.method == "POST":

        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")

        sales = Sale.objects.filter(
            created_at__date__gte=date_from, created_at__date__lte=date_to
        )
        if len(sales) > 0:
            sales_df = pd.DataFrame(sales.values())
            sales_df = sales_df.to_html()
            positions_data = []
            for sale in sales:
                for pos in sale.positions.all():
                    positions_data.append({
                        'id': pos.id,
                        'product_name': pos.product.name,
                        'quantity': pos.quantity,
                        'total_price': pos.price
                    })
            positions_df = pd.DataFrame(positions_data)
            positions_df = positions_df.to_html()

    context['form'] = SaleSearchForm(request.POST or None)
    context['sales_df'] = sales_df
    context['positions_df'] = positions_df
    return render(request=request, template_name="sales/home.html", context=context)


class SalesListView(ListView):
    model = Sale
    template_name = "sales/sales_list.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
