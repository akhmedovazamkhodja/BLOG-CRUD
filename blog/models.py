from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=400)
    text = models.TextField()
    image_1 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    date = models.DateField(auto_now=True) #datefield only used to store year
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True) #datetimefield used to store both year and times

    def __str__(self):
        return f"{self.post} - {self.body[:5]}"