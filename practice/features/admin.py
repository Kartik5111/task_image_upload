from django.contrib import admin
from .models import ImageUpload

class image_up(admin.ModelAdmin):
    list_display=('image','uploaded_at')
admin.site.register(ImageUpload,image_up)