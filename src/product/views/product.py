from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.forms import *
from product.models import *


class BaseProductView(generic.View):
    form_class = ProductForm
    model = Product
    template_name = 'products/create.html'
    success_url = '/product/products'


class ProductView(BaseProductView, ListView):
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Product.objects.filter(**filter_string)
              
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class ProductCreateView(BaseProductView, CreateView):
    pass


class ProductEditView(BaseProductView, UpdateView):
    pk_url_kwarg = 'id'
