# Generated by Django 2.2.6 on 2019-11-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191117_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_product', unique=True),
        ),
    ]