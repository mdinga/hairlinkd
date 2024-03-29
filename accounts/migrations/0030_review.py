# Generated by Django 3.2.2 on 2021-09-21 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_alter_stylist_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterion_1', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('comment', models.TextField(blank=True, max_length=128, null=True)),
                ('recommendation', models.BooleanField(blank=True, null=True)),
                ('total_rating', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.stylist')),
            ],
        ),
    ]
