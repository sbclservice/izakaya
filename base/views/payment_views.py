from django.views.generic import ListView
from base.models import Order, User
import json
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderPaymentView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/payment.html'
    context_object_name = 'payment'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return redirect("index")
        return Order.objects.filter(user=self.kwargs["id"],
            account_at__isnull=True,
            canceled_at__isnull=True
        )
    
    def get_served_items(self, order):
        return [item for item in json.loads(order.items) if item.get('served') != 1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id"] = self.kwargs["id"]

        # Get all items from filtered orders excluding served items
        items = []
        total_amount = 0
        total_tax_included = 0

        for order in context['payment']:
            served_items = self.get_served_items(order)
            items.extend(served_items)
            # Calculate total amount and total tax included excluding served items
            total_amount += sum(item['price'] * item['quantity'] for item in served_items)
            total_tax_included += sum(item['price'] * item['quantity'] * 1.1 for item in served_items)

        context["items"] = items
        context["total_amount"] = total_amount
        context["total_tax_included"] = total_tax_included

        return context


    def post(self, request, *args, **kwargs):
            id = self.kwargs.get("id")
            # Handle POST request logic here
            # For example, you might want to update the order status or perform some other action

            # Redirect to the same page or another page after processing the POST request
            return redirect('payment', id )  # Change 'your_redirect_view_name' to the actual name or URL of the view you want to redirect to


class OrderPaidView(LoginRequiredMixin, ListView):
    def post(self, request, *args, **kwargs):
            id = self.kwargs.get("id")

            # Find orders with the specified user ID and where account_at is None
            orders_to_update = Order.objects.filter(user=id, account_at__isnull=True)

            # Update the account_at field for each order
            for order in orders_to_update:
                order.account_at = timezone.now()
                order.save()


            user = User.objects.get(id=id)
            if user.is_admin == False:
                user.is_active = False
                user.save()
                user.is_active = True
                user.save()


            return redirect('payment', id)

