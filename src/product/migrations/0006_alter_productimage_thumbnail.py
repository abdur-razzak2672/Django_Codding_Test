# Generated by Django 4.0 on 2022-07-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productimage_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='thumbnail',
            field=models.CharField(max_length=255),
        ),
    ]
