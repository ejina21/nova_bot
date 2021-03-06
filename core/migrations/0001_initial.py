# Generated by Django 4.0.6 on 2022-07-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('tg_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='ID пользователя')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Логин пользователя')),
                ('is_get_contact', models.BooleanField(default=False, verbose_name='Оставил контакт')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
