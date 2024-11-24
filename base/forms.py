from django import forms
from django.contrib.auth import get_user_model
from .models import Item, Category


class UserCreationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', )

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'image', 'category']
    def __init__(self, *args, **kwargs):
        super(ItemCreationForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['image'].widget.attrs['multiple'] = True


class ItemCountForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['stock']


class ItemSortForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['sort']


class ItemCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['slug', 'name']
