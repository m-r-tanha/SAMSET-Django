# Generated by Django 2.2.5 on 2020-01-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Keyword', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('CV', models.TextField()),
            ],
        ),
    ]