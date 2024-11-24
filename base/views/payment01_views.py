from base.models import Order
import json
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class OrderPayment01View(LoginRequiredMixin, TemplateView):
    template_name = 'pages/payment01.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_admin:
            return redirect("index")

        user_ids = [
            1,
            2,
            3,
            4,
            5,
            6,
            # Add more user IDs as needed
        ]

        user_info_list = []

        for user_id in user_ids:
            user_orders = Order.objects.filter(user=user_id, account_at__isnull=True, canceled_at__isnull=True)
            served_items = []

            for order in user_orders:
                items = json.loads(order.items)
                served_items.extend([item for item in items if item.get('served') != 1])

            total_tax_included = sum(order.tax_included for order in user_orders)
            total_amount_excluding_served = sum(item['price'] * item['quantity'] for item in served_items)
            
            user_info = {
                'username': f'座席{user_ids.index(user_id) + 1}',
                'total_tax_included': total_tax_included,
                'total_amount_excluding_served': total_amount_excluding_served,
                'user_idd': user_id - 1,
                'user_id': user_id,
                'items': served_items,
            }

            user_info_list.append(user_info)

        context['user_info_list'] = user_info_list
        return context

# Your other views here (if any)
