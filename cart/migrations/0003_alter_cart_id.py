# Generated by Django 4.2.3 on 2023-07-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]