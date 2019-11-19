# Generated by Django 2.2.7 on 2019-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=100)),
            ],
        ),
    ]
