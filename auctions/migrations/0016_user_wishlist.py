# Generated by Django 3.1 on 2020-09-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_remove_user_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(to='auctions.Listing'),
        ),
    ]
