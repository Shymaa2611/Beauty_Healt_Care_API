# Generated by Django 4.2.3 on 2023-07-19 21:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_product_desc_alter_brand_brand_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='customer',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='customer',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'product')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'product')},
        ),
    ]
