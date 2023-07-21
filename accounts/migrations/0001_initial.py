# Generated by Django 4.2.3 on 2023-07-20 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user/avater/')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True, verbose_name='Gender')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('skin_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Skin Type')),
                ('skin_ton', models.CharField(blank=True, max_length=50, null=True, verbose_name='Skin Ton')),
                ('skin_concern', models.CharField(blank=True, max_length=50, null=True, verbose_name='Skin Concern')),
                ('hair_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='hair type')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]