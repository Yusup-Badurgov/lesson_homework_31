# Generated by Django 4.1.7 on 2023-03-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=80, null=True, verbose_name='Латтитуда')),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=80, null=True, verbose_name='Лонгитуда')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='Никнейм')),
                ('password', models.CharField(max_length=64, unique=True, verbose_name='Пароль')),
                ('role', models.CharField(choices=[('member', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], max_length=9)),
                ('age', models.PositiveSmallIntegerField()),
                ('location', models.ManyToManyField(to='user.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]