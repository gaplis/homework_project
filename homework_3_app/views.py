from django.shortcuts import render
from django.views.generic import TemplateView
from homework_2_app.models import Order, Client
from datetime import datetime, timedelta


# Create your views here.
class FindOrdersClient(TemplateView):
    template_name = 'homework_3_app/orders_client.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['client_id'])
        orders = Order.objects.filter(customer=client)
        context['title'] = f'Заказы клиента {client.name}, id: {client.pk}'
        context['orders'] = orders
        return context


class OrdersWeekClient(TemplateView):
    template_name = 'homework_3_app/orders_by_date.html'

    def get_context_data(self, **kwargs):
        enddate = datetime.now()
        startdate = enddate - timedelta(days=7)
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['client_id'])
        orders = Order.objects.filter(customer=client, date_ordered__range=[startdate, enddate])
        products = []
        for order in orders:
            for product in order.products.all():
                products.append(product)
        context['title'] = f'Товары клиента {client.name}, id: {client.pk} заказанные за последнюю неделю'
        context['products'] = set(products)
        return context


class OrdersMonthClient(TemplateView):
    template_name = 'homework_3_app/orders_by_date.html'

    def get_context_data(self, **kwargs):
        enddate = datetime.now()
        startdate = enddate - timedelta(days=30)
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['client_id'])
        orders = Order.objects.filter(customer=client, date_ordered__range=[startdate, enddate])
        products = []
        for order in orders:
            for product in order.products.all():
                products.append(product)
        context['title'] = f'Товары клиента {client.name}, id: {client.pk} заказанные за последний месяц'
        context['products'] = set(products)
        return context


class OrdersYearClient(TemplateView):
    template_name = 'homework_3_app/orders_by_date.html'

    def get_context_data(self, **kwargs):
        enddate = datetime.now()
        startdate = enddate - timedelta(days=365)
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['client_id'])
        orders = Order.objects.filter(customer=client, date_ordered__range=[startdate, enddate])
        products = []
        for order in orders:
            for product in order.products.all():
                products.append(product)
        context['title'] = f'Товары клиента {client.name}, id: {client.pk} заказанные за последний год'
        context['products'] = set(products)
        return context
