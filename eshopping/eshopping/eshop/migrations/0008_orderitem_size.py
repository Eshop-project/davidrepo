# Generated by Django 3.1 on 2020-12-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0007_auto_20201130_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.IntegerField(blank=True, default=8, null=True),
        ),
    ]
