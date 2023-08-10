# Generated by Django 4.1.4 on 2022-12-23 15:01

from django.db import migrations, models
import django.db.models.deletion
import main_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True)),
                ('surname', models.CharField(db_index=True, max_length=20, unique=True)),
                ('staff', models.CharField(db_index=True, max_length=20, unique=True)),
                ('photo', models.ImageField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('desc', models.TextField(blank=True, max_length=200)),
                ('photo', models.ImageField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField()),
                ('is_visible', models.BooleanField(default=True)),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True)),
                ('surname', models.CharField(db_index=True, max_length=20, unique=True)),
                ('prof', models.CharField(db_index=True, max_length=20, unique=True)),
                ('photo', models.ImageField()),
                ('resp', models.TextField(blank=True, max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Why_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField()),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('num',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('ingredients', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('photo', models.ImageField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
