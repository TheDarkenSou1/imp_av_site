# Generated by Django 4.1.7 on 2023-08-05 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_remove_about_back_img_alter_about_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='img',
        ),
    ]
