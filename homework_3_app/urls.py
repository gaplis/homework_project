from django.urls import path
from .views import FindOrdersClient, OrdersWeekClient, OrdersMonthClient, OrdersYearClient

urlpatterns = [
    path('client/<int:client_id>/', FindOrdersClient.as_view(), name='client'),
    path('client/week/<int:client_id>/', OrdersWeekClient.as_view(), name='week'),
    path('client/month/<int:client_id>/', OrdersMonthClient.as_view(), name='month'),
    path('client/year/<int:client_id>/', OrdersYearClient.as_view(), name='year')
]