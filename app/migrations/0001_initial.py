# Generated by Django 4.2.5 on 2023-10-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('engine', models.CharField(max_length=40)),
            ],
        ),
    ]
