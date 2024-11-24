from django.views.generic import ListView
from base.models import Order, Category
import json
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

class OrderIndexView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/orders.html'
    context_object_name = 'orders'

    
    
    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user,
            account_at__isnull=True,
            canceled_at__isnull=True
        )
    


    def get_served_items(self, order):
        return [item for item in json.loads(order.items) if item.get('served') != 1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # カテゴリのクエリセットを追加

        # Get all items from filtered orders excluding served items
        items = []
        total_amount = 0
        total_tax_included = 0

        for order in context['orders']:
            served_items = self.get_served_items(order)
            items.extend(served_items)
            # Calculate total amount and total tax included excluding served items
            total_amount += sum(item['price'] * item['quantity'] for item in served_items)
            total_tax_included += sum(item['price'] * item['quantity'] * 1.1 for item in served_items)

        context["items"] = items
        context["total_amount"] = total_amount
        context["total_tax_included"] = total_tax_included

        return context

