from django.contrib import admin

# Register your models here.
from .models import Hello
from .models import Image

admin.site.register(Hello)
admin.site.register(Image)
