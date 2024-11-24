from django.shortcuts import redirect
from base.forms import ItemCountForm, ItemSortForm
from django.urls import reverse
from django.views.generic import TemplateView
from base.models import Item
from django.views.decorators.http import require_POST

class ItemCountView(TemplateView):
    template_name = 'pages/item1111.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        context['form'] = ItemCountForm()  # Add the form to the context
        context['forms'] = ItemSortForm()  # Add the form to the context
        return context

def UpdateCount(request, pk):
    if request.method == "POST":
        form = ItemCountForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['stock']
            Item.objects.update_or_create(pk=pk, defaults={"stock": stock})
            return redirect(reverse('item1111'))
    return redirect(reverse('item1111'))  # Handle non-POST or invalid form cases


def UpdateSort(request, pk):
    if request.method == "POST":
        form = ItemSortForm(request.POST)
        if form.is_valid():
            sort = form.cleaned_data['sort']
            Item.objects.update_or_create(pk=pk, defaults={"sort": sort})
            return redirect(reverse('item1111'))
    return redirect(reverse('item1111'))  # Handle non-POST or invalid form cases



@require_POST#ボタンが押された時のみ動作する。
def Delitem(request,pk):
    delitem = Item.objects.get(id=pk)
    delitem.is_published = False
    delitem.save()
    return redirect(reverse('item1111'))
