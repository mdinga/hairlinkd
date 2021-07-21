# Generated by Django 3.2.2 on 2021-05-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stylist_app', '0004_auto_20210512_1131'),
        ('accounts', '0010_stylist_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylist',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, through='accounts.ProductOffering', to='stylist_app.Product'),
        ),
    ]
