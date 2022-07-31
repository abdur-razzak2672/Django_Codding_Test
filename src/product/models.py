from django.db import models
from config.g_model import TimeStampMixin
from django.db import models



# Create your models here.
class Variant(TimeStampMixin):
    id = models.AutoField(primary_key = True,editable = False)
    title = models.CharField(max_length =255 ,null =True, blank =True)
    description = models.TextField(null =True, blank =True)
    created_at = models.DateTimeField(auto_now_add =True)
    Updated_at = models.DateTimeField(auto_now_add =False, null =True, blank =True)


class Product(TimeStampMixin):
    id = models.AutoField(primary_key = True,editable = False)
    title = models.CharField(max_length =255 ,null =True, blank =True)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null =True, blank =True)
    created_at = models.DateTimeField(auto_now_add =True)
    Updated_at = models.DateTimeField(auto_now_add =False, null =True, blank =True)
    


class ProductImage(TimeStampMixin):
    id = models.AutoField(primary_key = True,editable = False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null =True)
    file_path = models.URLField()
    created_at = models.DateTimeField(auto_now_add =True)
    Updated_at = models.DateTimeField(auto_now_add =False, null =True, blank =True)
    


class ProductVariant(TimeStampMixin):
    id = models.AutoField(primary_key = True,editable = False)
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add =True)
    Updated_at = models.DateTimeField(auto_now_add =False, null =True, blank =True)


class ProductVariantPrice(TimeStampMixin):
    id = models.AutoField(primary_key = True,editable = False)
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add =True)
    Updated_at = models.DateTimeField(auto_now_add =False, null =True, blank =True)
