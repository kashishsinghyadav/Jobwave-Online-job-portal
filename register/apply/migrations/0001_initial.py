# Generated by Django 4.2.2 on 2023-07-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_icon', models.CharField(max_length=80)),
                ('apply_info', models.CharField(max_length=80)),
                ('apply_desc', models.TextField()),
            ],
        ),
    ]
