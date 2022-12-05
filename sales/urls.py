from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('sales-list/', views.SalesListView.as_view(), name='sales_list_view'),
    path('sale-detail/<str:pk>', views.SaleDetailView.as_view(), name='sale_detail_view'),
]
