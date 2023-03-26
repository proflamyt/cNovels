from django.contrib.gis.db import models
from django.contrib.gis.db.models.fields import PolygonField
from authors.models import AuthorModel
from django.conf import settings
from django.urls import reverse

# Create your models here.
class NovelModel(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(AuthorModel, related_name='books')
    readers_num = models.IntegerField(blank=True, null=True)
    ratings = models.IntegerField(default=5.0)
    image = models.ImageField(null=True)
    weekly_featured = models.BooleanField(default=False)
    special_featured = models.BooleanField(default=False)
    pubished = models.BooleanField(default=True)
    maptype = models.ForeignKey('MapType', on_delete=models.CASCADE, null=True, blank=True)
    date_uploaded = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    

    class Meta():
        ordering = ["-date_uploaded"]


    def __str__(self) -> str:
        return self.title
    

class Goal(models.Model):
    book = models.ForeignKey(NovelModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type_choices = (
        ('reading', 'Reading'),
        ('reviewing', 'Reviewing'),
        ('discussing', 'Discussing')
    )
    goal_type = models.CharField(max_length=20, choices=goal_type_choices)
    target_date = models.DateField()

    class Meta:
        unique_together = ('book', 'user')
    

class ChapterModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    book = models.ForeignKey(NovelModel, on_delete=models.CASCADE, related_name='chapters')
    content = models.TextField(null=True)
    date_uploaded = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    


class MapType(models.Model):
    name = models.CharField(max_length=30)
    

    def get_absolute_url(self):    
        return reverse('points', args=[str(self.novel_id), str(self.id)])

    def __str__(self) -> str:
        return self.name


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = models.PointField()
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, null=True, blank=True)
    maptype  = models.ForeignKey(MapType, blank=True,null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    chapter = models.ManyToManyField(ChapterModel, related_name='chapters')

    def __str__(self):
        """Return string representation."""
        return self.name





class Area(models.Model):
    name = models.CharField(max_length=255)
    location = PolygonField()
    description = models.TextField()
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,null=True, blank=True)
    chapter = models.ManyToManyField(ChapterModel, related_name='chapter_areas')

 


class SnapShots(models.Model):
    novel = models.ForeignKey(NovelModel, on_delete=models.CASCADE, related_name='snap_images')
    image = models.ImageField(upload_to='book_images/')

    class Meta:
        verbose_name_plural = 'book images'

    def __str__(self):
        return f"{self.novel.title} image {self.id}"
    


class UserBook(models.Model):

    STATUS_CHOICES = [
        ('u', 'unread'),
        ('r', 'read'),
        ('f', 'finished'),
    ]
    book = models.ForeignKey(NovelModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    can_read = models.BooleanField(default=False)
    state = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='u')