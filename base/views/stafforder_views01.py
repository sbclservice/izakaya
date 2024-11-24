from django.views.generic import ListView
from base.models import Order
import json
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



class OrderStaffView01(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/order0000.html'
    context_object_name = 'orders0000'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return redirect("index")
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter orders with both account_at and canceled_at as None
        filtered_orders = [
            order for order in context['orders0000']
            if order.account_at is None and order.canceled_at is None
        ]

        items = []
        shipping = []
        total_amount = 0
        total_tax_included = 0

        for order in filtered_orders:
            order_items = json.loads(order.items)

            # Modify each item to include the username
            for item in order_items:
                item['username'] = order.user.username
                item['created_at'] = order.created_at
                item['ord'] = order.id


            items.extend(order_items)
            shipping.extend(json.loads(order.shipping))

            total_amount += order.amount
            total_tax_included += order.tax_included

        context["items"] = items
        context["shipping"] = shipping
        context["total_amount"] = total_amount
        context["total_tax_included"] = total_tax_included

        return context

    def test_func(self):
        # Check if the user is an admin
        return self.request.user.is_admin
    
