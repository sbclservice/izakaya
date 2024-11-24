from django.views.generic import ListView, DetailView
from base.models import Item, Category, Tag


class IndexListView(ListView):
    # model = Item
    template_name = 'pages/index.html'
    # queryset = Item.objects.filter(is_published=True)  # 追記
    # ordering = ['sort']  # Add this line to order items by the 'sort' field
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.filter(is_published=True).order_by('sort')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # カテゴリのクエリセットを追加
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'
    queryset = Item.objects.filter(is_published=True)  # 追記


class CategoryListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 4
    ordering = ['sort']  # Add this line to order items by the 'sort' field
 
 
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['pk'])
        return Item.objects.filter(is_published=True, category=self.category)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Category #{self.category.name}'
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # カテゴリのクエリセットを追加
        return context
 
 
class TagListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 2
 
    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        return Item.objects.filter(is_published=True, tags=self.tag)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Tag #{self.tag.name}"
        return context