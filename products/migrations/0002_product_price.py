# Generated by Django 4.1.2 on 2022-12-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, help_text='Amount in Rs.'),
            preserve_default=False,
        ),
    ]
