# Generated by Django 4.0 on 2022-07-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='Updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='Updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]