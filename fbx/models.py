from django.db import models

# Create your models here.

from django.db import models

class Fbx(models.Model):
    name = models.CharField(max_length=200)
    fbx = models.FileField(max_length=200, blank=True)
    normals = models.FileField(max_length=200, blank=True)
    bump = models.FileField(max_length=200, blank=True)
    texture = models.FileField(max_length=200, blank=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)


