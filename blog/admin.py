from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)       # Allow the model to be visible on admin page.
