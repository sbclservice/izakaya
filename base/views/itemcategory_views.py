from django.views.generic import View
from django.shortcuts import render, redirect
from base.models import Category
from base.forms import ItemCategoryForm
from django.urls import reverse


class ItemCategoryView(View):
    def get(self, request, *args, **kwargs):
        form = ItemCategoryForm(request.POST or None)
        return render(request, 'pages/itemcate.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ItemCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            member = Category(
                slug=form.cleaned_data['slug'],
                name=form.cleaned_data['name']
            )
            member.save()
            return redirect(reverse('itemcate'))
        return render(request, 'pages/itemcate.html', {'form': form})