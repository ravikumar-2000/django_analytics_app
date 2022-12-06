from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from customers.models import Customer
from profiles.models import Profile
from .forms import SaleSearchForm
from .utils import get_chart
import pandas as pd


def home_view(request):
    context = {}
    sales_df = None
    positions_df = None
    merged_df = None
    summarized_df = None
    chart = None

    if request.method == "POST":

        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")

        sales = Sale.objects.filter(
            created_at__date__gte=date_from, created_at__date__lte=date_to
        )
        if len(sales) > 0:
            sales_df = pd.DataFrame(sales.values())
            sales_df["customer_id"] = sales_df["customer_id"].apply(
                lambda x: Customer.objects.get(id=x).name
            )
            sales_df["sales_person_id"] = sales_df["sales_person_id"].apply(
                lambda x: Profile.objects.get(id=x).user.username
            )
            sales_df["created_at"] = sales_df["created_at"].apply(
                lambda x: x.strftime("%Y-%m-%d")
            )
            sales_df["updated_at"] = sales_df["updated_at"].apply(
                lambda x: x.strftime("%Y-%m-%d")
            )
            sales_df.rename(
                {
                    "customer_id": "customer",
                    "sales_person_id": "sales person",
                    "id": "sales_id",
                },
                axis=1,
                inplace=True,
            )
            positions_data = []
            for sale in sales:
                for pos in sale.positions.all():
                    positions_data.append(
                        {
                            "position_id": pos.id,
                            "product_name": pos.product.name,
                            "quantity": pos.quantity,
                            "position_total_price": pos.price,
                            "sales_id": pos.get_sales_id(),
                        }
                    )
            positions_df = pd.DataFrame(positions_data)
            merged_df = pd.merge(sales_df, positions_df, on="sales_id")
            summarized_df = merged_df.groupby(by="transaction_id", as_index=False)[
                "position_total_price"
            ].agg("sum")
            chart = get_chart(chart_type=chart_type, data=summarized_df)

            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()

    context["form"] = SaleSearchForm(request.POST or None)
    context["sales_df"] = sales_df
    context["positions_df"] = positions_df
    context["merged_df"] = merged_df
    context["chart"] = chart
    return render(request=request, template_name="sales/home.html", context=context)


class SalesListView(ListView):
    model = Sale
    template_name = "sales/sales_list.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/sale_detail.html"
