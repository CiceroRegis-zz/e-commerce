# Generated by Django 2.2.6 on 2019-11-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191117_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='fatured',
            new_name='featured',
        ),
    ]