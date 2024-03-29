# Generated by Django 3.2.2 on 2021-05-11 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_alter_stylist_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hairstyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('BLOW_WAVE', 'Blow-Wave'), ('HAIR_TREATMENT', 'Hair Treatment'), ('HAIR_INSTALLATION', 'Hair Installation'), ('NATURAL_HAIR', 'Natural Hair'), ('HAIR_STYLING', 'Hair Styling'), ('HAIRCUT', 'Haircut'), ('COLOURING', 'Colouring'), ('WIG', 'Wig'), ('UNCATERGORISED', 'Uncatergorised')], default='Uncatergorised', max_length=128)),
                ('description', models.TextField(blank=True, max_length=254)),
                ('hairstyle_image', models.ImageField(blank=True, upload_to='hairstyle_eg/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('WIGS', 'Wigs'), ('FIBRE', 'Fibre'), ('HAIRCARE', 'Hair Care'), ('UNCATERGORISED', 'Uncatergorised')], default='Uncatergorised', max_length=128)),
                ('description', models.TextField(blank=True, max_length=254)),
                ('product_image', models.ImageField(blank=True, upload_to='product_eg/')),
            ],
        ),
        migrations.CreateModel(
            name='StylistProductOffering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=254)),
                ('price', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_offering', to='stylist_app.product')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stylist_product', to='accounts.stylist')),
            ],
            options={
                'unique_together': {('product', 'stylist')},
            },
        ),
        migrations.CreateModel(
            name='StylistHairOffering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=254)),
                ('price', models.FloatField(blank=True, null=True)),
                ('hairstyle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='style_offering', to='stylist_app.hairstyle')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stylist_hairstyle', to='accounts.stylist')),
            ],
            options={
                'unique_together': {('hairstyle', 'stylist')},
            },
        ),
    ]
