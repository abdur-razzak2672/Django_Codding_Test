# Generated by Django 4.0 on 2022-07-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='DEFAULT VALUE', max_length=140),
        ),
    ]