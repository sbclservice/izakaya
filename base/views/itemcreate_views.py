from django.views.generic import View
from django.shortcuts import render, redirect
from base.models import Item
from base.forms import ItemCreationForm
from django.urls import reverse


class ItemCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ItemCreationForm(request.POST or None)
        return render(request, 'pages/item0000.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ItemCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if an image was provided
            if 'image' in request.FILES:
                member = Item(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    sort=999,
                    stock=999999,
                    description=form.cleaned_data['description'],
                    sold_count=0,
                    is_published=True,
                    image=form.cleaned_data['image'],
                    category=form.cleaned_data['category']
                )
                member.save()
                return redirect(reverse('item0000'))
            else:
                # Handle the case where no image was provided
                form.add_error('image', 'Please provide an image.')
        # Form is not valid, render the form again with errors
        return render(request, 'pages/item0000.html', {'form': form})