# Generated by Django 4.2.1 on 2023-05-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Denoise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
