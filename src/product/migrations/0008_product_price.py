# Generated by Django 4.0 on 2022-07-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_productimage_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='DEFAULT VALUE', max_length=140),
        ),
    ]