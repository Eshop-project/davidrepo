# Generated by Django 3.1.1 on 2020-10-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eShop', '0002_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
