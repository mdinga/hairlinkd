# Generated by Django 3.2.2 on 2021-05-12 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stylist_app', '0003_auto_20210511_1816'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serviceoffering',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='serviceoffering',
            name='hairstyle',
        ),
        migrations.RemoveField(
            model_name='serviceoffering',
            name='stylist',
        ),
        migrations.DeleteModel(
            name='ProductOffering',
        ),
        migrations.DeleteModel(
            name='ServiceOffering',
        ),
    ]
