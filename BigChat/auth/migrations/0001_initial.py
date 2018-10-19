# Generated by Django 2.1.1 on 2018-10-19 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]