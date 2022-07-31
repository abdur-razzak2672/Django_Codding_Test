from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput

from product.models import *


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
      
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
      
class ProductVariantForm(ModelForm):
    class Meta:
        model = ProductVariant
        fields = '__all__'
        
class ProductVariantPriceForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
         