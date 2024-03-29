# Generated by Django 3.1.2 on 2020-12-21 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='land_parcel', related_query_name='land_parcel', to='parcels.parcels', verbose_name='Parcels')),
            ],
            options={
                'verbose_name_plural': 'ownership',
                'db_table': 'ownership',
            },
        ),
    ]
