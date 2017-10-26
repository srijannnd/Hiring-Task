from .models import Customer, Order
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


def index(request):
    customers_list = list()
    number_of_orders_list = list()
    manufacturers_list = list()
    total_cost_list = list()

    total_cost = int()
    manufacturers = list()

    for customer in Customer.objects.all():
        orders = Order.objects.filter(Q(name=customer))
        number_of_orders = orders.count()
        number_of_orders_list.append(number_of_orders)
        customers_list.append(customer.name)

        for i in orders:
            manufacturers.append(i.manufacturer.upper())
            total_cost += i.total_price_per_order()

        total_cost_list.append(total_cost)
        manufacturers_list.append(', '.join(set(manufacturers)))
        manufacturers = list()
        total_cost = 0

    zipped = zip(customers_list, number_of_orders_list, total_cost_list, manufacturers_list)

    return render(request, 'mysite/order_list.html', {'zipped': zipped})