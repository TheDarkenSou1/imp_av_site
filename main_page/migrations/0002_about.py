# Generated by Django 4.1.4 on 2022-12-29 13:17

import django.core.validators
from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_img', models.ImageField()),
                ('phone_num', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Некоректно введено номер телефону.', regex='(^\\+38)?(-|\\s)?(\\d{3})(-|\\s)?(\\d{3})(-|\\s)?(\\d{2})(-|\\s)?(\\d{2})')])),
                ('desc', models.TextField(blank=True, max_length=500)),
                ('img', models.ImageField()),
                ('video_link', models.CharField(max_length=1000)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]
