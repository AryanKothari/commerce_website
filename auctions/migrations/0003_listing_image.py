# Generated by Django 3.1 on 2020-09-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='listing_pics'),
        ),
    ]