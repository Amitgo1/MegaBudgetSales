# Generated by Django 4.2.1 on 2023-05-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_myuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
