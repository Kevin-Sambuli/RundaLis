# Generated by Django 3.1.2 on 2021-04-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20201222_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='parcel_no',
            field=models.IntegerField(verbose_name='Parcel No'),
        ),
    ]
