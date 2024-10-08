from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Picture(models.Model):
    TAG_CATEGORY = [
        ('people', 'People'),
        ('nature', 'Nature'),
        ('food', 'Food'),
        ('animal', 'Animal'),
        ('lifestyle', 'Lifestyle')
    ]


    title = models.CharField(max_length=100)
    my_pic = CloudinaryField('image')
    description = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_photo', blank=True)
    tag_category = models.CharField(max_length=50, choices=TAG_CATEGORY, default='nature')

    def __str__(self):
        return self.title
    

