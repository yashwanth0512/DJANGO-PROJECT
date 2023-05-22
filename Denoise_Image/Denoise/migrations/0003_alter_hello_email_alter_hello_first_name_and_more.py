# Generated by Django 4.2.1 on 2023-05-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Denoise', '0002_hello'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email ID'),
        ),
        migrations.AlterField(
            model_name='hello',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='hello',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='hello',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
    ]
