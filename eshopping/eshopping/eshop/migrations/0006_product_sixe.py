# Generated by Django 3.1.1 on 2020-11-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_product_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sixe',
            field=models.IntegerField(blank=True, default=8, null=True),
        ),
    ]