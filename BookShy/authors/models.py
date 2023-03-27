from django.db import models
from django.conf import settings

# Create your models here.

class AuthorModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=23, db_index=True, null=True)
    weekly_featured = models.BooleanField(default=False)
    special_featured = models.BooleanField(default=True)
    




