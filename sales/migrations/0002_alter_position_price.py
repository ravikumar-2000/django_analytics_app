# Generated by Django 4.1.2 on 2022-12-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
