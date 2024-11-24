from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from base.models import Item, Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
import json
 
 
 
 
class PaySuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/success.html'
 
    def get(self, request, *args, **kwargs):
        # 最新のOrderオブジェクトを取得し、注文確定に変更
        order = Order.objects.filter(
            user=request.user).order_by('-created_at')[0]
        order.is_confirmed = True  # 注文確定
        order.save()
 
        # カート情報削除
        del request.session['cart']
 
        return super().get(request, *args, **kwargs)
 
 
 
 
def create_line_item(unit_amount, name, category, quantity):
    return {
        'price_data': {
            'currency': 'JPY',
            'unit_amount': unit_amount,
            'product_data': {'name': name, }
        },
        'quantity': quantity,
        'tax_rates': settings.TAX_RATE
    }
 
 
class ConfirmedView(LoginRequiredMixin, View):
 
    def post(self, request, *args, **kwargs):

        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            return redirect('/')
 
        items = []  # Orderモデル用に追記
        line_items = []
        for item_pk, quantity in cart['items'].items():
            item = Item.objects.get(pk=item_pk)
            line_item = create_line_item(
                item.price, item.name, item.category, quantity)
            line_items.append(line_item)
 
            # Orderモデル用に追記
            items.append({
                'pk': item.pk,
                'name': item.name,
                'image': str(item.image),
                'price': item.price,
                'category':item.category.slug,
                'quantity': quantity,
                'cook': False,
                'served': False,
            })
 
            # 在庫をこの時点で引いておく、注文キャンセルの場合は在庫を戻す
            # 販売数も加算しておく
            item.stock -= quantity
            item.sold_count += quantity
            item.save()
 
        # 仮注文を作成（is_confirmed=Flase)
        Order.objects.create(
            user=request.user,
            uid=request.user.pk,
            items=json.dumps(items),
            shipping=serializers.serialize("json", [request.user.profile]),
            amount=cart['total'],
            tax_included=cart['tax_included_total']
        )
 

        return redirect('success')