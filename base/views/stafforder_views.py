from django.views.generic import ListView
from base.models import Order
import json
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.timezone import localtime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class OrderStaffView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return redirect(reverse("index"))
        return Order.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filter orders with both account_at and canceled_at as None
        filtered_orders = [
            order for order in context['orders']
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
    

@require_POST
def CookingView(request, id, pk):
    order = get_object_or_404(Order, id=id)
    
    # Load the 'items' from JSON and handle both dictionary and list cases
    items = json.loads(order.items)
    if not isinstance(items, list):
        items = []

    # Find the item in the items list/dictionary with the matching pk
    for item in items:
        if isinstance(item, dict) and item.get('pk') == pk:
            # Update the 'quantity' field with the desired value (e.g., 4)
            item['cook'] = localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            order.items = json.dumps(items)  # Convert back to JSON string
            order.save()  # Save the changes to the Order instance
            break
    
    return redirect('order')




@require_POST
def ServedView(request, id, pk):
    order = get_object_or_404(Order, id=id)
    
    # Load the 'items' from JSON and handle both dictionary and list cases
    items = json.loads(order.items)
    if not isinstance(items, list):
        items = []

    # Find the item in the items list/dictionary with the matching pk
    for item in items:
        if isinstance(item, dict) and item.get('pk') == pk:
            # Update the 'quantity' field with the desired value (e.g., 4)
            item['served'] = localtime(timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
            order.items = json.dumps(items)  # Convert back to JSON string
            order.save()  # Save the changes to the Order instance
            break
    
    return redirect('order')



@require_POST
def CancelView(request, id, pk):
    order = get_object_or_404(Order, id=id)
    
    # Load the 'items' from JSON and handle both dictionary and list cases
    items = json.loads(order.items)
    if not isinstance(items, list):
        items = []

    # Find the item in the items list/dictionary with the matching pk
    for item in items:
        if isinstance(item, dict) and item.get('pk') == pk:
            # Update the 'quantity' field with the desired value (e.g., 4)
            item['served'] = 1
            order.items = json.dumps(items)  # Convert back to JSON string
            order.save()  # Save the changes to the Order instance
            break
    
    return redirect('order')