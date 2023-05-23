# Generated by Django 4.1.7 on 2023-03-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=150)),
                ('year_of_birth', models.IntegerField(blank=True, null=True)),
                ('year_of_death', models.IntegerField(blank=True, null=True)),
                ('country_of_origin', models.CharField(default='Unknown', max_length=25)),
            ],
        ),
    ]
