from django.urls import path
from django.views.generic import TemplateView

from product.views.product import *
from product.views.variant import *
from product.views.productVariant import *

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('products/', ProductView.as_view(), name='products'),
    path('product/create', ProductCreateView.as_view(), name='create.product'),
    path('product/<int:id>/edit', ProductEditView.as_view(), name='update.product'),
    
    # Productsvariant URLs
    path('productVariants/', ProductVariantView.as_view(), name='productVariants'),
    path('productVariants/create', ProductVariantCreateView.as_view(), name='create.product'),
    path('productVariants/<int:id>/edit', ProductVariantEditView.as_view(), name='update.product'),
    
    # Productsvariant URLs
    path('productVariantsPrice/', ProductVariantView.as_view(), name='productVariantsPrice'),
    path('productVariantsPrice/create', ProductVariantCreateView.as_view(), name='create.product'),
    path('productVariantsPrice/<int:id>/edit', ProductVariantEditView.as_view(), name='update.product'),
    
    
    
]
