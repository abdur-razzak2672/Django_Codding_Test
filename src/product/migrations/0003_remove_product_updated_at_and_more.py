# Generated by Django 4.0 on 2022-07-31 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_variant_active_product_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Updated_at',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='Updated_at',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='Updated_at',
        ),
    ]
