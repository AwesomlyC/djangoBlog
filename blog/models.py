from django.db import models        # For creating SQL Objects
from django.conf import settings    
from django.utils import timezone   # For retrieving the correct timezone relevent to PST (UTC-8)

# Create your models here.

# Similar to creating a class (Object) in MySQL --> SQLite3
# models.Model --> define Post as a Django Model to be saved in the database.
class Post(models.Model):
    """
        Attributes:
            author          -       Foreign Key
            title           -       CharField(200)
            text            -       TextField()
            created_date    -       DateTimeField
            published_date  -       DateTimeField
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Methods
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Overriding
    def __str__(self):
        return self.title