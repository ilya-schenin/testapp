# Generated by Django 5.0.1 on 2024-01-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('adress', models.CharField(max_length=255)),
                ('postcode', models.IntegerField()),
            ],
        ),
    ]