# Generated by Django 3.2.5 on 2021-07-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
