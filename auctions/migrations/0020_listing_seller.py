# Generated by Django 3.1 on 2020-09-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='seller',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
