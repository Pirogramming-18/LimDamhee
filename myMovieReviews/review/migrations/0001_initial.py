# Generated by Django 2.0.13 on 2023-01-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=20)),
                ('character', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('star', models.FloatField()),
                ('time', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]
