# Generated by Django 4.0 on 2022-07-31 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_updated_at_productimage_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='thumbnail',
            field=models.BooleanField(default=False),
        ),
    ]
