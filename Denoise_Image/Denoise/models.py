from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Hello(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email ID')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')

    def __str__(self):
        return self.first_name

# Create your models here.
