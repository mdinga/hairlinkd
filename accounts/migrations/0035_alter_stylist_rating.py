# Generated by Django 3.2.2 on 2021-09-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_alter_stylist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylist',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]