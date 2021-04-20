# Generated by Django 3.1.2 on 2021-04-07 20:00

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centroids',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('perimeter', models.FloatField()),
                ('area_ha', models.FloatField()),
                ('lr_no', models.CharField(max_length=10)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name_plural': 'centroid',
                'db_table': 'centroids',
            },
        ),
    ]