# Generated by Django 3.1.14 on 2023-08-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products_api", "0002_auto_20230803_1750"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="url",
            field=models.TextField(max_length=1000),
        ),
    ]
